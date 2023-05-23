import pygame
import random

YELLOW = ((255,255,0))
PURPLE = ((240,0,255, 40))
SKY_BLUE = ((0,255,255))
TILESIZE = 32

# BOARD = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
#         ,
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
#         ,
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
#         ,
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
#         ]

BOARD_WIDTH = 10
BOARD_HEIGHT = 10

# Define the probability bias for the values
PROBABILITY_BIAS = {
    0: 0.8,  # Probability for 0 (empty cell)
    1: 0.2   # Probability for 1 (wall)
}

# Generate the random map layout with probability bias
BOARD = [[0] + random.choices([0, 1], [PROBABILITY_BIAS[0], PROBABILITY_BIAS[1]], k=BOARD_HEIGHT-1) for _ in range(BOARD_WIDTH)]
S_WIDTH = TILESIZE * len(BOARD)
S_HEIGHT = TILESIZE * len(BOARD[0])



SCREEN = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
pygame.display.set_caption("Albertus Adventures")
CLOCK = pygame.time.Clock()
