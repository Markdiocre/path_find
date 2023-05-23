import pygame

from player import Pickle,Cat, Fish
from grid import Grid
from settings import *
import random
import math


from path_find import astar



def main():

    pygame.init()

    #game dimensionsr
    
    running  = True
    dt = 0 
    

    grid = Grid()
    cat = Cat(1,0,1, SCREEN)
    pickle = Pickle(8,7,1)
    fish = Fish()

    all_sprite = pygame.sprite.Group()
    all_sprite.add(cat)
    all_sprite.add(pickle)
    all_sprite.add(fish)

    clock = pygame.time.get_ticks()
    move_next_time = clock + 500

    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock = pygame.time.get_ticks()

        player_center = pygame.Vector2(cat.rect.center)

        # Relative position of mouse
        mouse_pos = pygame.mouse.get_pos()
        fish.capture_mouse(mouse_pos[0],mouse_pos[1])
        delta = mouse_pos - player_center

        # Calculate the angle 
        angle_to_mouse = (round(math.degrees(math.atan2(delta.y, delta.x))) + 360) % 360

        
        

        if ( clock > move_next_time ): 
            if angle_to_mouse > 225 and angle_to_mouse <= 315: cat.move_up()
            if angle_to_mouse > 45 and angle_to_mouse <=135: cat.move_down()
            if angle_to_mouse > 135 and angle_to_mouse <= 225: cat.move_left()
            if angle_to_mouse <= 45 or angle_to_mouse >= 315: cat.move_right()
            move_next_time = clock + 500

            

            #Tracks a star every second
            pickle_to_cat_path = astar(BOARD, (pickle.x, pickle.y) ,(cat.x,cat.y))
            if len(pickle_to_cat_path) > 1:
                pickle.move(pickle_to_cat_path[1][0],pickle_to_cat_path[1][1])
            
            #If the cat ate the player, the player will teleport elsewhere
            if((cat.x,cat.y) == (pickle.x,pickle.y)):
                out_of_pos = True
                while out_of_pos:
                    x = random.randint(0,len(BOARD)-1)
                    y = random.randint(0,len(BOARD[0])-1)

                    if BOARD[x][y] != 1:
                        cat.x = x
                        cat.y = y
                        out_of_pos = False

        SCREEN.fill((0,0,0))

        # cat.draw()
        # pickle.draw()
        grid.draw_grid()

        all_sprite.update()
        all_sprite.draw(SCREEN)

        

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = CLOCK.tick(60) / 1000

if __name__ == '__main__':
    main()
    pygame.quit()