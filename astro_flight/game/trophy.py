import arcade
import random
from game import constants


class Trophy(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale, hit_box_algorithm='Detailed')
        self.center_x = random.randint(10, constants.SCREEN_WIDTH - 10)
        self.center_y = random.randint(10, constants.SCREEN_HEIGHT - 50)
