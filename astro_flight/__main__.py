# Imports
import arcade
from game import constants
from game.constructor import Constructor

# Classes
class Game(arcade.Window):
    """Main Game window
    """
    def __init__(self):
        """Initialize the window
        """
        
        # Call the parent class constructor
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # Set the background color
        self.background = arcade.load_texture("astro_flight/game/images/background.png")
        
        # Setup
        self.constructor = Constructor()     
    
    def on_update(self, delta_time):
        self.constructor.all_sprites.update()
        
        # Keep the constructor.player on screen
        if self.constructor.player.top > constants.SCREEN_HEIGHT:
            self.constructor.player.top = constants.SCREEN_HEIGHT
        if self.constructor.player.right > constants.SCREEN_WIDTH:
            self.constructor.player.right = constants.SCREEN_WIDTH
        if self.constructor.player.bottom < 0:
            self.constructor.player.bottom = 0
        if self.constructor.player.left < 0:
            self.constructor.player.left = 0
        
        # Collision detection
        if self.constructor.player.collides_with_list(self.constructor.asteroids_list):
            arcade.close_window()
    
    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        W/A/S/D: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.constructor.player.change_y = 8

        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            self.constructor.player.change_y = -8

        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.constructor.player.change_x = -8

        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.constructor.player.change_x = 8

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (
            symbol == arcade.key.W
            or symbol == arcade.key.S
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.constructor.player.change_y = 0

        if (
            symbol == arcade.key.A
            or symbol == arcade.key.D
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.constructor.player.change_x = 0
    
    def on_draw(self):
        """Called whenever you need to draw your window
        """

        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        self.constructor.all_sprites.draw()
        
    
    
# Main code entry point
if __name__ == "__main__":
    app = Game()
    arcade.run()