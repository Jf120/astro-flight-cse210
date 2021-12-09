import arcade
from game import constants

class Lives(arcade.Sprite):
    """Create life object
    """
    
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        
        # Positioning
        self.center_y = 760
    
    def update(self):
        
        super().update()
    
