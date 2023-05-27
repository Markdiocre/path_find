import pygame

from player import Pickle, Cat, Fish
from grid import Grid
from settings import *
import random
import math


from path_find import astar


class HealthBar():
    def __init__(self, x, y, w, h, max_hp) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(SCREEN, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(
            SCREEN, "green", (self.x, self.y, self.w * ratio, self.h))


health_bar = HealthBar(S_WIDTH - 70, 10, 60, 30, 3)

star_image = pygame.image.load("assets/star.png")
star_image = pygame.transform.scale(star_image, (TILESIZE, TILESIZE))


def init_point():
    no_pos = True
    while no_pos:
        x = random.randint(0, len(BOARD)-1)
        y = random.randint(0, len(BOARD[0])-1)

        if BOARD[x][y] != 1:
            rect = pygame.Rect(x * TILESIZE, y *TILESIZE, TILESIZE, TILESIZE)
            SCREEN.blit(star_image, rect)
            no_pos = False


def main():
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()

    # backgroud music
    pygame.mixer.music.load("assets/Music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # game dimensionsr

    running = True
    is_paused = False
    dt = 0
    settings = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    background_image = pygame.image.load("assets/bg2.png")
    background_image = pygame.transform.scale(
        background_image, (S_WIDTH, S_HEIGHT))
    flicker_interval = 1500
    flicker_timer = 0
    is_visible = True

    grid = Grid()
    cat = Cat(1, 0, 1, SCREEN)
    pickle = Pickle(8, 7, 1)
    fish = Fish()

    all_sprite = pygame.sprite.Group()
    all_sprite.add(cat)
    all_sprite.add(pickle)
    all_sprite.add(fish)

    clock = pygame.time.get_ticks()
    move_next_time = clock + 500

    pygame.mouse.set_cursor(
        (8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

    is_dead = False
    score = 0

    init_point()

    while running:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_paused = not is_paused
                if event.key == pygame.K_ESCAPE:
                    running = False

            if is_dead:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        is_dead = False
                        score = 0
                        health_bar.hp = health_bar.max_hp
                        init_point()
                    elif event.key == pygame.K_q:
                        running = False

        # Game over Screen
        if not is_paused and is_dead:
            settings.blit(background_image, (0, 0))
            font = pygame.font.Font("assets/font.ttf", 15)
            game_over = font.render("Game Over", True, 'red')
            score_text = font.render(
                "Your Score: " + str(score), True, 'white')
            retry_text = font.render(
                "Press 'R' to Retry", True, 'yellow')
            quit_text = font.render(
                "Press 'Q' to Quit", True, 'yellow')
            settings.blit(game_over, (S_WIDTH // 2 - 80, S_HEIGHT // 2 - 90))
            settings.blit(score_text, (S_WIDTH // 2 - 80, S_HEIGHT // 2 - 65))
            settings.blit(retry_text, (S_WIDTH // 2 - 80, S_HEIGHT // 2 - 40))
            settings.blit(quit_text, (S_WIDTH // 2 - 80, S_HEIGHT // 2 - 15))


        if not is_paused and not is_dead:
            clock = pygame.time.get_ticks()

            player_center = pygame.Vector2(cat.rect.center)

            # Relative position of mouse
            mouse_pos = pygame.mouse.get_pos()
            fish.capture_mouse(mouse_pos[0], mouse_pos[1])
            delta = mouse_pos - player_center

            # Calculate the angle
            angle_to_mouse = (
                round(math.degrees(math.atan2(delta.y, delta.x))) + 360) % 360
            
            

            if (clock > move_next_time):
                if angle_to_mouse > 225 and angle_to_mouse <= 315:
                    cat.move_up()
                if angle_to_mouse > 45 and angle_to_mouse <= 135:
                    cat.move_down()
                if angle_to_mouse > 135 and angle_to_mouse <= 225:
                    cat.move_left()
                if angle_to_mouse <= 45 or angle_to_mouse >= 315:
                    cat.move_right()

                # Tracks a star every second
                if (random.randint(0, 5) != 1):  # This line is for balancing
                    pickle_to_cat_path = astar(
                        BOARD, (pickle.x, pickle.y), (cat.x, cat.y))
                    if len(pickle_to_cat_path) > 1:
                        pickle.move(
                            pickle_to_cat_path[1][0], pickle_to_cat_path[1][1])

                # If the cat ate the player, the player will teleport elsewhere
                if ((cat.x, cat.y) == (pickle.x, pickle.y)):
                    out_of_pos = True
                    while out_of_pos:
                        x = random.randint(0, len(BOARD)-1)
                        y = random.randint(0, len(BOARD[0])-1)

                        if BOARD[x][y] != 1:
                            cat.x = x
                            cat.y = y
                            out_of_pos = False

                    if (health_bar.hp - 1 <= 0):
                        is_dead = True
                    else:
                        health_bar.hp = health_bar.hp - 1

                score += 1
                move_next_time = clock + 500

            SCREEN.fill((0, 0, 0))

            # cat.draw()
            # pickle.draw()
            grid.draw_grid()

            all_sprite.update()

            health_bar.draw()

            pygame.draw.line(SCREEN, (255, 255, 255),
                             player_center, mouse_pos, 3)
            
            font = pygame.font.Font("assets/font.ttf", 15)
            score_text = font.render(str(score), True, 'yellow')
            settings.blit(score_text, ( S_WIDTH // 2, 10))

            # Spawn Points

            all_sprite.draw(SCREEN)

            # flip() the display to put your work on screen
            pygame.display.flip()

        # Click P to pause
        if is_paused and not is_dead:
            settings.blit(background_image, (0, 0))
            font = pygame.font.Font("assets/font.ttf", 15)
            pause_text1 = font.render("Game Paused", True, 'yellow')
            flicker_timer += pygame.time.get_ticks()
            if pygame.time.get_ticks() % flicker_interval < flicker_interval // 2:
                is_visible = True
            else:
                is_visible = False
            if is_visible:
                pause_text2 = font.render("Press P to Resume", True, 'yellow')
                text_rect = pause_text2.get_rect(
                    center=(S_WIDTH // 2, S_HEIGHT // 2 - 40))
                settings.blit(pause_text2, text_rect)
            settings.blit(pause_text1, (S_WIDTH // 2 - 80, S_HEIGHT // 2 - 90))

        # flip() the display to put your work on screen
        pygame.display.flip()


if __name__ == '__main__':
    main()
    pygame.quit()
