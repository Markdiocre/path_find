import pygame

YELLOW = ((255,255,0))
PURPLE = ((240,0,255, 40))
SKY_BLUE = ((0,255,255))
TILESIZE = 32

BOARD = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        ,
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        ,
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        ,
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        ]


S_WIDTH = TILESIZE * len(BOARD)
S_HEIGHT = TILESIZE * len(BOARD[0])



SCREEN = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
pygame.display.set_caption("Albertus Adventures")
CLOCK = pygame.time.Clock()
