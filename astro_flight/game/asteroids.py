import arcade
import random
from game import constants

# Where on the screen will the asteroids come out from
positions = [1, constants.SCREEN_WIDTH]

class Asteroid(arcade.Sprite):
    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale, hit_box_algorithm='Detailed')
        self.center_x = random.choice(positions)
        self.center_y = random.randint(10, constants.SCREEN_HEIGHT - 10)
        
        # Set its speed to a random speed heading left
        if self.center_x == 1:
            self.velocity = (random.randint(2, 8), 0)
        else:
            
            # Set its speed to a random speed heading right
            self.velocity = (random.randint(-8, -2), 0)
    
    def update(self):
        """Update the position of the sprite
        When it moves off screen, remove it
        """

        # Move the sprite
        super().update()

        # Remove if off the screen
        if self.center_x < 1 or self.center_x > constants.SCREEN_WIDTH:
            self.remove_from_sprite_lists()