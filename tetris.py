import pygame
import random

pygame.init()

# ---------------------------------------------------------
# Mobile / Touch Configuration
# ---------------------------------------------------------
# Dynamic height adapting to aspect ratio
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700

# Board Dimensions (Standard Tetris: 10x20)
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 28  # Pixels per grid square

BOARD_X = (SCREEN_WIDTH - (GRID_WIDTH * BLOCK_SIZE)) // 2
BOARD_Y = 50

# Colors
BLACK = (15, 15, 20)
WHITE = (240, 240, 240)
GRAY = (50, 50, 60)
LIGHT_GRAY = (80, 80, 95)
CYAN = (0, 240, 240)
BLUE = (0, 0, 240)
ORANGE = (240, 160, 0)
YELLOW = (240, 240, 0)
GREEN = (0, 240, 0)
PURPLE = (160, 0, 240)
RED = (240, 0, 0)

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]]  # O
]

COLORS = [CYAN, RED, GREEN, PURPLE, ORANGE, BLUE, YELLOW]


class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = COLORS[SHAPES.index(shape)]

    def rotate(self):
        # Rotate matrix clockwise
        self.shape = [list(row) for row in zip(*self.shape[::-1])]


def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid


def valid_space(piece, grid):
    accepted_positions = [[(x, y) for x in range(GRID_WIDTH) if grid[y][x] == BLACK] for y in range(GRID_HEIGHT)]
    accepted_positions = [pos for sub in accepted_positions for pos in sub]

    formatted = []
    for y, row in enumerate(piece.shape):
        for x, val in enumerate(row):
            if val:
                formatted.append((piece.x + x, piece.y + y))

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] >= 0:  # Allow piece to spawn above screen
                return False
    return True


def clear_rows(grid, locked):
    cleared = 0
    for y in range(GRID_HEIGHT - 1, -1, -1):
        if BLACK not in grid[y]:
            cleared += 1
            # Remove locked positions in this row
            for x in range(GRID_WIDTH):
                del locked[(x, y)]
            # Shift every row above down
            for (lx, ly) in list(locked.keys()):
                if ly < y:
                    color = locked.pop((lx, ly))
                    locked[(lx, ly + 1)] = color
    return cleared


def draw_button(surface, rect, text, color=GRAY):
    pygame.draw.rect(surface, color, rect, border_radius=8)
    pygame.draw.rect(surface, LIGHT_GRAY, rect, width=2, border_radius=8)
    font = pygame.font.SysFont('sans-serif', 28, bold=True)
    txt_obj = font.render(text, True, WHITE)
    txt_rect = txt_obj.get_rect(center=rect.center)
    surface.blit(txt_obj, txt_rect)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mobile Tetris")
    clock = pygame.time.Clock()

    locked_positions = {}
    grid = create_grid(locked_positions)

    current_piece = Piece(3, 0, random.choice(SHAPES))
    fall_time = 0
    fall_speed = 0.45  # Seconds per step
    score = 0
    game_over = False

    # ---------------------------------------------------------
    # Touch Control Button Zones (Bottom Half of Screen)
    # ---------------------------------------------------------
    btn_left = pygame.Rect(30, 610, 70, 60)
    btn_right = pygame.Rect(180, 610, 70, 60)
    btn_down = pygame.Rect(105, 630, 70, 50)
    btn_rotate = pygame.Rect(280, 610, 90, 60)

    while not game_over:
        grid = create_grid(locked_positions)
        dt = clock.tick(60) / 1000.0
        fall_time += dt

        # Automatic Gravity Downward Movement
        if fall_time >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid):
                current_piece.y -= 1
                # Lock Piece
                for y, row in enumerate(current_piece.shape):
                    for x, val in enumerate(row):
                        if val:
                            locked_positions[(current_piece.x + x, current_piece.y + y)] = current_piece.color

                cleared = clear_rows(grid, locked_positions)
                score += cleared * 100

                current_piece = Piece(3, 0, random.choice(SHAPES))
                if not valid_space(current_piece, grid):
                    game_over = True

        # Touch & Key Input Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Screen Touch Detection
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.FINGERDOWN):
                if event.type == pygame.FINGERDOWN:
                    px, py = event.x * SCREEN_WIDTH, event.y * SCREEN_HEIGHT
                else:
                    px, py = event.pos

                if btn_left.collidepoint(px, py):
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif btn_right.collidepoint(px, py):
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1

                elif btn_down.collidepoint(px, py):
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                elif btn_rotate.collidepoint(px, py):
                    current_piece.rotate()
                    if not valid_space(current_piece, grid):
                        # Undo rotation if invalid
                        for _ in range(3):
                            current_piece.rotate()

        # Render background
        screen.fill(BLACK)

        # Draw Title and Score
        font = pygame.font.SysFont('sans-serif', 28)
        score_txt = font.render(f"SCORE: {score}", True, WHITE)
        screen.blit(score_txt, (BOARD_X, 15))

        # Draw Grid & Locked Blocks
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = (BOARD_X + x * BLOCK_SIZE, BOARD_Y + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, grid[y][x], rect)
                pygame.draw.rect(screen, GRAY, rect, 1)

        # Draw Active Piece
        for y, row in enumerate(current_piece.shape):
            for x, val in enumerate(row):
                if val:
                    rect = (BOARD_X + (current_piece.x + x) * BLOCK_SIZE,
                            BOARD_Y + (current_piece.y + y) * BLOCK_SIZE,
                            BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(screen, current_piece.color, rect)
                    pygame.draw.rect(screen, WHITE, rect, 1)

        # Draw On-Screen Control Buttons
        draw_button(screen, btn_left, "◄")
        draw_button(screen, btn_right, "►")
        draw_button(screen, btn_down, "▼")
        draw_button(screen, btn_rotate, "ROTATE", color=(40, 100, 180))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
