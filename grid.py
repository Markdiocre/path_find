import pygame
from settings import *

class Grid(object):
    def draw_grid(self):
        for x in range(len(BOARD)):
            for y in range(len(BOARD[x])):
                rect = pygame.Rect(x*(TILESIZE), y*(TILESIZE), TILESIZE, TILESIZE)
                if BOARD[x][y] == 1:
                    pygame.draw.rect(SCREEN, (0,255,170), rect)
                if BOARD[x][y] == 2:
                    pygame.draw.rect(SCREEN, YELLOW, rect)
                if BOARD[x][y] == 3:
                    pygame.draw.rect(SCREEN, PURPLE, rect)
                if BOARD[x][y] == 4:
                    pygame.draw.rect(SCREEN, SKY_BLUE, rect)
                else:
                    pygame.draw.rect(SCREEN, (255,255,255), rect, 1)
