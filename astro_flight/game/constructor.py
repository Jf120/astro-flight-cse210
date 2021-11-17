import arcade
import random
from game import constants
from game.spaceship import Spaceship
from game.asteroids import Asteroid

class Constructor:
    """The director is the main game loop
    """

    def __init__(self):
        """Get the game ready to play
        """
        self.asteroids_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        # Set up the player
        self.player = Spaceship("astro_flight\game\images\spaceship.png", constants.SCALING)
        self.all_sprites.append(self.player)

        # Set asteroids
        # Spawn a new asteroid 0.25 seconds
        arcade.schedule(self.add_enemy, 0.25)
    
    def add_enemy(self, delta_time: float):
        enemy = Asteroid("astro_flight\game\images\obstacle.png", random.choice(constants.ASTEROID_SCALING))
        self.asteroids_list.append(enemy)
        self.all_sprites.append(enemy)