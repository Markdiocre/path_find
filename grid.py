import pygame
from settings import *
import os

img_folder = os.path.join( "assets")
wall_image = pygame.image.load("assets/wall_sprite.png")
wall_image = pygame.transform.scale(wall_image, (TILESIZE, TILESIZE))

class Grid(object):
    def draw_grid(self):
        for x in range(len(BOARD)):
            for y in range(len(BOARD[x])):
                rect = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                if BOARD[x][y] == 1:
                    SCREEN.blit(wall_image, rect)
                else:
                    pygame.draw.rect(SCREEN, (255, 255, 255), rect, 1)
