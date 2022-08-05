import pygame
from pygame import Surface


class User:
    moveSpeed = 0.5
    state = "neutral"
    states = []

    def __init__(self, x, y, image: Surface, delta_time):
        self.x = x
        self.y = y
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.delta_time = delta_time

    def set_state(self, state):
        self.state = state

    def move_left(self):
        if self.x > 0:
            self.x -= self.moveSpeed * self.delta_time

    def move_right(self):
        if self.x < 400 - self.image.get_width():
            self.x += self.moveSpeed * self.delta_time

    def set_delta_time(self, delta_time):
        self.delta_time = delta_time

    def on_key_up(self, key):
        if key == pygame.K_LEFT:
            self.states = [state for state in self.states if state != key]

        if key == pygame.K_RIGHT:
            self.states = [state for state in self.states if state != key]

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

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
            player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            is_collision = pygame.Rect.colliderect(player_rect, rect)
            if is_collision is True:
                return is_collision

            return False
