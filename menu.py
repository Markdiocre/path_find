import pygame
from pygame.locals import *
import main
import os

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

s_width=320
s_height=320
screen=pygame.display.set_mode((s_width, s_height))
BG = pygame.image.load("assets/bg2.png").convert()
bg_width = BG.get_width()
bg_rect = BG.get_rect()

def text_format(message, textFont, textSize, textColor):
    Font=pygame.font.Font(textFont, textSize)
    Text=Font.render(message, 0, textColor)

    return Text

font = "assets/font.ttf"

clock = pygame.time.Clock()
FPS=60

def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        menu = False  # Set menu variable to False to exit the menu loop and close the menu
                        main.main()  # Start the main game from the imported main module

                    if selected == "quit":
                        pygame.quit()
                        quit()

        screen.blit(BG, (0, 0))
        title1=text_format("Albertus", font, 25, "yellow")
        title2=text_format("Adventures", font, 25, "yellow")
        if selected=="start":
            start=text_format("START", font, 22, "white")
        else:
            start = text_format("START", font, 15, "black")
        if selected=="quit":
            quit=text_format("QUIT", font, 22, "white")
        else:
            quit = text_format("QUIT", font, 15, "black")

        title1_rect=title1.get_rect()
        title2_rect=title1.get_rect()
        start_rect=start.get_rect()
        quit_rect=quit.get_rect()

        screen.blit(title1, (s_width/2 - (title1_rect[2]/2), 50))
        screen.blit(title2, (s_width/2 - (title2_rect[2]/1.6), 90))
        screen.blit(start, (s_width/2 - (start_rect[2]/2), 175))
        screen.blit(quit, (s_width/2 - (quit_rect[2]/2), 225))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Albertus Adventures")

main_menu()
pygame.quit()
quit()