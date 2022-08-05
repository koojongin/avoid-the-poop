import pygame
from pygame import Surface
from pygame.mixer import Sound
from pygame.surface import SurfaceType


class User:
    moveSpeed = 0.1
    state = "neutral"
    states = []

    def __init__(self, x, y, image: Surface | SurfaceType, delta_time):
        self.x = x
        self.y = y
        self.image = image
        self.delta_time = delta_time

    def set_state(self, state):
        self.state = state

    def move_left(self):
        if self.x > 0:
            self.x -= 0.1 * self.delta_time

    def move_right(self):
        if self.x < 400 - self.image.get_width():
            self.x += 0.1 * self.delta_time

    def set_delta_time(self, delta_time):
        self.delta_time = delta_time

    def on_key_up(self, key):
        if key == pygame.K_LEFT:
            self.states.remove(key)

        if key == pygame.K_RIGHT:
            self.states.remove(key)

        if pygame.K_LEFT in self.states:
            self.state = "left"

        if pygame.K_RIGHT in self.states:
            self.state = "right"

        if self.states.__len__() == 0:
            self.state = "neutral"

    def on_key_down(self, key):
        if key == pygame.K_LEFT:
            self.states.append(key)
            self.state = "left"

        if key == pygame.K_RIGHT:
            self.states.append(key)
            self.state = "right"
