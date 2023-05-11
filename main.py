import pygame

from player import Player,Cat
from grid import Grid
from settings import *
import random


from path_find import astar

def main():

    pygame.init()

    #game dimensionsr
    
    running  = True
    dt = 0 
    

    grid = Grid()
    player = Player(0,0,1, SCREEN)
    cat = Cat(8,7,1)

    clock = pygame.time.get_ticks()
    move_next_time = clock + 500

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock = pygame.time.get_ticks()
        cat_to_player_path = []
        last_pos = (player.x, player.y)

        if ( clock > move_next_time ): 
            pressed = pygame.key.get_pressed() 
            if pressed[pygame.K_UP]: player.move_up()
            if pressed[pygame.K_DOWN]: player.move_down()
            if pressed[pygame.K_LEFT]: player.move_left()
            if pressed[pygame.K_RIGHT]: player.move_right()
            move_next_time = clock + 500

            #Tracks a star every second
            cat_to_player_path = astar(BOARD, (cat.x, cat.y) ,(player.x,player.y))
            if len(cat_to_player_path) > 1:
                cat.move(cat_to_player_path[1][0],cat_to_player_path[1][1])
            
            #If the cat ate the player, the player will teleport elsewhere
            if((player.x,player.y) == (cat.x,cat.y)):
                out_of_pos = True
                while out_of_pos:
                    x = random.randint(0,len(BOARD)-1)
                    y = random.randint(0,len(BOARD[0])-1)

                    if BOARD[x][y] != 1:
                        player.x = x
                        player.y = y
                        out_of_pos = False

        SCREEN.fill((0,0,0))

        player.draw()
        cat.draw()
        grid.draw_grid()

        

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = CLOCK.tick(60) / 1000

if __name__ == '__main__':
    main()
pygame.quit()