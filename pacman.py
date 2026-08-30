import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for Android Screen (Adjustable)
SCREEN_WIDTH = 250
SCREEN_HEIGHT = 00
GRID_SIZE = 30
FPS = 10

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Simple Maze Layout (1 = Wall, 0 = Pellet)
MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
]