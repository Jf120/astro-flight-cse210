import arcade
import random
from game import constants
from game.spaceship import Spaceship
from game.asteroids import Asteroid
from game.trophy import Trophy

class Constructor:
    """Creates sprites
    """

    def __init__(self):
        """Get the game ready to play
        """
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Obstacles")
        

        # Set up the player
        self.player = Spaceship(constants.PATH + "\images\spaceship.png", constants.SCALING)
        self.scene.add_sprite("Player", self.player)

        # Set asteroids
        self.resume()
        
        # set trophy
        self.trophy = Trophy(constants.PATH + "\images\prize.png", constants.TROPHY_SCALING)
        self.scene.add_sprite("Trophy", self.trophy)
    
    def add_enemy(self, delta_time: float):
        """Add an asteroid instance to the scene
        """
        
        enemy = Asteroid(constants.PATH + "\images\obstacle.png", random.choice(constants.ASTEROID_SCALING))
        self.scene.add_sprite("Obstacles", enemy)
        
    def pause(self):
        
        """Pause the game
        """
        
        # Unschedule the asteroid spawner
        arcade.unschedule(self.add_enemy)
    
    def resume(self):
        """Resume the game
        """
        
        # Spawn a new asteroid 0.25 seconds
        arcade.schedule(self.add_enemy, 0.25)