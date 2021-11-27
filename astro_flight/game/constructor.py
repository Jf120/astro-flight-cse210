import arcade
import random
from game import constants
from game.spaceship import Spaceship
from game.asteroids import Asteroid

class Constructor:
    """Creates sprites
    """

    def __init__(self):
        """Get the game ready to play
        """
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Obstacles")
        

        # Set up the player
        self.player = Spaceship("astro_flight\game\images\spaceship.png", constants.SCALING)
        self.scene.add_sprite("Player", self.player)

        # Set asteroids
        self.resume()
    
    def add_enemy(self, delta_time: float):
        enemy = Asteroid("astro_flight\game\images\obstacle.png", random.choice(constants.ASTEROID_SCALING))
        self.scene.add_sprite("Obstacles", enemy)
        
    def pause(self):
        """Pause the game
        """
        arcade.unschedule(self.add_enemy)
    
    def resume(self):
        """Resume the game
        """
        
        # Spawn a new asteroid 0.25 seconds
        arcade.schedule(self.add_enemy, 0.25)