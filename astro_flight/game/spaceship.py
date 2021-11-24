import arcade
from game import constants

class Spaceship(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.speed = 0
        self.max_speed = 10
        self.center_x = constants.SCREEN_WIDTH / 2
        self.center_y = constants.SCREEN_HEIGHT / 10

    def update(self):
        """Update the position of the sprite
        Keep it from moving off the screen
        """
        
        # Moves the player
        super().update()
        
        # Keep the player on screen
        if self.top > constants.SCREEN_HEIGHT:
            self.top = constants.SCREEN_HEIGHT
        if self.right > constants.SCREEN_WIDTH:
            self.right = constants.SCREEN_WIDTH
        if self.bottom < 0:
            self.bottom = 0
        if self.left < 0:
            self.left = 0
    
    