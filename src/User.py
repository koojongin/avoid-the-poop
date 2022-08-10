import pygame
from pygame import Surface


class User:
    moveSpeed = 0.5
    to_x = 0
    screen = None

    def __init__(self, x, y, image: Surface, delta_time):
        self.x = x
        self.y = y
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.delta_time = delta_time

    def set_screen(self, screen):
        self.screen = screen

    def set_delta_time(self, delta_time):
        self.delta_time = delta_time

    def on_key_up(self, key):
        self.to_x = 0

    def on_key_down(self, key):
        if key == pygame.K_LEFT:
            self.to_x -= self.moveSpeed

        if key == pygame.K_RIGHT:
            self.to_x += self.moveSpeed

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
            player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            is_collision = pygame.Rect.colliderect(player_rect, rect)
            if is_collision is True:
                return is_collision

            return False

    def update(self):
        move_delta = self.to_x * self.delta_time
        if self.x + move_delta <= 0:
            move_delta = 0

        if self.x + move_delta >= self.screen.get_width() - self.width:
            move_delta = 0

        self.x += move_delta
