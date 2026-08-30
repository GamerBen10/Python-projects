import pygame
import sys

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 448
FPS = 60

# Colors
COLOR_SKY = (107, 140, 255)
COLOR_MARIO = (230, 40, 40)
COLOR_GROUND = (228, 116, 12)
COLOR_BLOCK = (252, 188, 116)
COLOR_COIN = (252, 216, 0)
COLOR_GOOMBA = (116, 76, 12)
COLOR_TEXT = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Mario Bros")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# -------------------------------------------------------------------
# PLAYER (MARIO) CLASS
# -------------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((28, 36))
        self.image.fill(COLOR_MARIO)
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Physics vectors
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 4
        self.jump_power = -12
        self.gravity = 0.6
        self.on_ground = False
        
        self.score = 0
        self.coins = 0

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += self.gravity
        if self.vel_y > 10:
            self.vel_y = 10  # Terminal velocity

    def update(self, blocks):
        self.get_input()
        self.apply_gravity()
        
        # Horizontal Movement & Collision
        self.rect.x += self.vel_x
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if self.vel_x > 0:  # Moving right
                    self.rect.right = block.rect.left
                elif self.vel_x < 0:  # Moving left
                    self.rect.left = block.rect.right

        # Vertical Movement & Collision
        self.rect.y += self.vel_y
        self.on_ground = False
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if self.vel_y > 0:  # Falling
                    self.rect.bottom = block.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:  # Jumping up into block
                    self.rect.top = block.rect.bottom
                    self.vel_y = 0
                    if isinstance(block, QuestionBlock):
                        block.hit(self)

# -------------------------------------------------------------------
# ENVIRONMENT BLOCKS
# -------------------------------------------------------------------
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width=32, height=32, color=COLOR_GROUND):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

class QuestionBlock(Block):
    def __init__(self, x, y):
        super().__init__(x, y, color=COLOR_BLOCK)
        self.has_item = True

    def hit(self, player):
        if self.has_item:
            self.has_item = False
            self.image.fill((150, 150, 150))  # Turn grey when hit
            player.score += 200
            player.coins += 1

# -------------------------------------------------------------------
# ENEMIES (GOOMBA)
# -------------------------------------------------------------------
class Goomba(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((28, 28))
        self.image.fill(COLOR_GOOMBA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = 1
        self.speed = 1.5

    def update(self, blocks):
        self.rect.x += self.direction * self.speed
        
        # Turn around on block collisions
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if self.direction > 0:
                    self.rect.right = block.rect.left
                    self.direction = -1
                elif self.direction < 0:
                    self.rect.left = block.rect.right
                    self.direction = 1

# -------------------------------------------------------------------
# LEVEL SETUP & MAIN LOOP
# -------------------------------------------------------------------
def build_level():
    blocks = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    
    # Ground
    for x in range(0, SCREEN_WIDTH * 2, 32):
        if x not in range(400, 496):  # Create a gap/pit
            blocks.add(Block(x, SCREEN_HEIGHT - 32))

    # Platforms and Question Blocks
    platform_data = [
        (200, 320), (232, 320), (264, 320),
        (500, 280), (532, 280), (564, 280),
    ]
    for x, y in platform_data:
        blocks.add(Block(x, y, color=COLOR_GROUND))
        
    question_blocks = [(232, 320), (532, 280), (600, 200)]
    for x, y in question_blocks:
        blocks.add(QuestionBlock(x, y - 96))

    # Enemies
    enemies.add(Goomba(350, SCREEN_HEIGHT - 60))
    enemies.add(Goomba(650, SCREEN_HEIGHT - 60))

    return blocks, enemies

def main():
    player = Player(50, SCREEN_HEIGHT - 100)
    player_group = pygame.sprite.GroupSingle(player)
    blocks, enemies = build_level()
    
    camera_offset_x = 0

    while True:
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 2. Logic Updates
        player.update(blocks)
        enemies.update(blocks)

        # Camera scroll tracking player
        if player.rect.centerx - camera_offset_x > SCREEN_WIDTH * 0.5:
            camera_offset_x = player.rect.centerx - SCREEN_WIDTH * 0.5

        # Player-Enemy Interactions
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                # Stomp Goomba (Player moving down and above enemy)
                if player.vel_y > 0 and player.rect.bottom <= enemy.rect.top + 12:
                    enemy.kill()
                    player.vel_y = -8  # Bounce off enemy
                    player.score += 100
                else:
                    # Player dies (restart level)
                    main()

        # Fall into pit
        if player.rect.top > SCREEN_HEIGHT:
            main()

        # 3. Drawing
        screen.fill(COLOR_SKY)

        # Draw all objects offset by camera
        for sprite in blocks:
            screen.blit(sprite.image, (sprite.rect.x - camera_offset_x, sprite.rect.y))
        for enemy in enemies:
            screen.blit(enemy.image, (enemy.rect.x - camera_offset_x, enemy.rect.y))
            
        screen.blit(player.image, (player.rect.x - camera_offset_x, player.rect.y))

        # UI Overlay
        score_surface = font.render(f"MARIO   WORLD 1-1   COINS: {player.coins:02d}   SCORE: {player.score:06d}", True, COLOR_TEXT)
        screen.blit(score_surface, (16, 16))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
