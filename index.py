import sys
from random import randrange

import pygame
from pygame import mixer

from src.Ddong import Ddong
from src.User import User

pygame.init()
mixer.init()

WHITE = (255, 255, 255)
WINDOW_TITLE = "똥피하기"
DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 650
USER_IMAGE_WIDTH = 20
USER_IMAGE_HEIGHT = 40

# init
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("arial", 30, True, False)
ddong_image = pygame.image.load("resources/images/ddong.png")
user_image = pygame.image.load("resources/images/user.png")
sound_bgm = pygame.mixer.Sound("resources/audio/bgm_server.mp3")
sound_poop = pygame.mixer.Sound('resources/audio/poop.wav')

#
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
sound_bgm.set_volume(0.5)
sound_poop.set_volume(0.5)
sound_bgm.play()


def create_ddong(x, y, image, sound):
    ddong = Ddong(x, y)
    ddong.set_image(image)
    ddong.set_sound(sound)
    return ddong


#
time_elapsed_since_last_action = 0
ddong_create_event = pygame.USEREVENT + 1
pygame.time.set_timer(ddong_create_event, 100)


def get_game_options():
    obstacles = []
    user = User(DISPLAY_WIDTH / 2 - USER_IMAGE_WIDTH / 2, DISPLAY_HEIGHT - USER_IMAGE_HEIGHT, user_image, 0)
    is_running_game = True

    return dict({'obstacles': obstacles, 'user': user, 'is_running_game': is_running_game})


options = get_game_options()
obstacles = options['obstacles']
user = options['user']
is_running_game = options['is_running_game']
avoid_score = 0

while True:

    if is_running_game is False:
        end_text = game_font.render("Dead!"
                                    "Press SpaceBar", True, (0, 0, 0))
        display.blit(end_text,
                     [DISPLAY_WIDTH / 2 - end_text.get_width() / 2, DISPLAY_HEIGHT / 2 - end_text.get_height() / 2])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    options = get_game_options()
                    obstacles = options['obstacles']
                    user = options['user']
                    is_running_game = options['is_running_game']
                    avoid_score = 0

        pygame.display.update()
        continue

    pygame.display.update()
    delta_time = clock.tick(60)
    score_text = game_font.render(str(avoid_score), True, (0, 0, 0))
    user.set_delta_time(delta_time)

    display.fill([255, 255, 255])
    display.blit(score_text, [0, 0])
    display.blit(user.image, (user.x, user.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == ddong_create_event:
            position_x = randrange(DISPLAY_WIDTH - ddong_image.get_width())
            _ddong = create_ddong(position_x, 0, ddong_image, sound_poop)
            obstacles.append(_ddong)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # user.set_state('left')
                user.on_key_down(event.key)

            if event.key == pygame.K_RIGHT:
                # user.set_state('right')
                user.on_key_down(event.key)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                user.on_key_up(event.key)

    for obstacle in obstacles:
        if obstacle is not None:
            display.blit(obstacle.image, obstacle.get_position())
            obstacle.fall(delta_time)
            if obstacle.is_dead:
                obstacles.remove(obstacle)
                avoid_score += 1

    if user.state == "left":
        user.move_left()

    if user.state == "right":
        user.move_right()

    is_collision = user.check_collision(obstacles)
    if is_collision is True:
        is_running_game = False
