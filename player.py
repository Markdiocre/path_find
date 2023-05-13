import pygame
from settings import *
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "assets")

class Cat(pygame.sprite.Sprite):
    
    def __init__(self,x,y,speed, surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"cat.png")).convert_alpha()
        BOARD[x][y] == 2
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect()
        


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
    
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    # def draw(self):
        
    #     self.rect = pygame.Rect(self.x*TILESIZE,self.y*TILESIZE, TILESIZE,TILESIZE)
    #     pygame.draw.rect(SCREEN, YELLOW, self.rect)
        # self.image.blit( self.surface, self.rect)

        

class Pickle(pygame.sprite.Sprite):
    
    def __init__(self,x,y,speed) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"pickle.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = speed
        BOARD[x][y] == 4

    def move(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pygame.sprite.Sprite):
    pass

class Fish(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"Fish.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.mid_height = (self.image.get_width()/2)
        self.mid_width = (self.image.get_height()/2)

    def capture_mouse(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x - (TILESIZE/2)
        self.rect.y = self.y - (TILESIZE/2)
        