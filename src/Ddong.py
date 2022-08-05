from pygame import Surface
from pygame.mixer import Sound


class Ddong:
    image = None
    sound = None
    width = 0
    height = 0
    is_dead = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def set_image(self, image: Surface):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()

    def fall(self, delta_time):
        death_line = 650
        if self.image is not None:
            if (self.y + self.height) >= death_line and self.is_dead is False:
                self.sound.play()
                self.is_dead = True

        self.y += 0.5 * delta_time

    def set_sound(self, sound: Sound):
        self.sound = sound
