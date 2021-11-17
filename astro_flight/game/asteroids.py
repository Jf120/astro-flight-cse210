import arcade
import random
from game import constants

positions = [5, 530]

class Asteroid(arcade.Sprite):
    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale)
        self.left = random.choice(positions)
        self.top = random.randint(10, constants.SCREEN_HEIGHT - 10)
        
        # Set its speed to a random speed heading left
        if self.left == 5:
            self.velocity = (random.randint(5, 15), 0)
        else:
            self.velocity = (random.randint(-15, -5), 0)
    
    def update(self):
        """Update the position of the sprite
        When it moves off screen to the left, remove it
        """

        # Move the sprite
        super().update()

        # Remove if off the screen
        if self.right < 0:
            self.remove_from_sprite_lists()
