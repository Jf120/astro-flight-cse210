import arcade
from game import constants

class Spaceship(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.speed = 0
        self.max_speed = 10
        self.center_x = constants.SCREEN_WIDTH / 2
        self.center_y = constants.SCREEN_HEIGHT / 10

