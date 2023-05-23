import pygame
from settings import *
import os

wall_image = pygame.image.load("assets/wall_sprite.png")
wall_image = pygame.transform.scale(wall_image, (TILESIZE, TILESIZE))


ground_image = pygame.image.load("assets/grass_tile.png")
ground_image = pygame.transform.scale(ground_image, (TILESIZE, TILESIZE))

class Grid(object):
    def draw_grid(self):
        for x in range(len(BOARD)):
            for y in range(len(BOARD[x])):
                rect = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                if BOARD[x][y] == 1:
                    SCREEN.blit(wall_image, rect)
                else:
                    SCREEN.blit(ground_image, rect)
