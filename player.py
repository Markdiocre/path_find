import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    
    def __init__(self,x,y,speed, surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets\cat.png').convert_alpha()
        BOARD[x][y] == 2
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect()
        self.surface = surface

        


    def move_up(self):
        if self.y - self.speed < 0:
            self.y = 0
            return

        if self.hits_grid(self.x, self.y - self.speed):
            self.y += -self.speed
        

    def move_down(self):
        if self.y + self.speed >= len(BOARD[0]):
            self.y = len(BOARD[0]) - 1


            return

        if self.hits_grid(self.x, self.y + self.speed):
            self.y += self.speed



    def move_left(self):
        if self.x - self.speed < 0:
            self.x = 0

            return

        if self.hits_grid(self.x - self.speed,self.y):
            self.x -= self.speed


    def move_right(self):
        if self.x + self.speed >= len(BOARD):
            self.x = len(BOARD) - 1
            return

        if self.hits_grid(self.x + self.speed,self.y):
            self.x += self.speed


    def hits_grid(self, x, y):
        if BOARD[x][y] == 1:
            return False
        return True
    

    def draw(self):
        
        self.rect = pygame.Rect(self.x*TILESIZE,self.y*TILESIZE, TILESIZE,TILESIZE)
        pygame.draw.rect(SCREEN, YELLOW, self.rect)
        # self.image.blit( self.surface, self.rect)

        

class Cat():
    
    def __init__(self,x,y,speed) -> None:
        self.rect = pygame.Rect(x*TILESIZE,y*TILESIZE, TILESIZE,TILESIZE)
        self.x = x
        self.y = y
        self.speed = speed
        BOARD[x][y] == 4

    def draw(self):
        self.rect = pygame.Rect(self.x*TILESIZE,self.y*TILESIZE, TILESIZE,TILESIZE)
        pygame.draw.rect(SCREEN, SKY_BLUE, self.rect)

    def move(self,x,y):
        self.x = x
        self.y = y
        