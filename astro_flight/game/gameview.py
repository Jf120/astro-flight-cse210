import arcade
import arcade.gui
from game import constants
from game.constructor import Constructor

class GameView(arcade.View):
    """Main Game window
    """
    def __init__(self):
        """Initialize the window
        """
        
        # Sets size of the window and title
        super().__init__()

        self.window.set_mouse_visible(False)
        
        # Variable with background image
        self.background = arcade.load_texture("astro_flight/game/images/background.png")
        
        # Setup game
    def setup(self):
        """Called when the view is loaded
        """
        self.constructor = Constructor()     
    
    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
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
    
    def on_update(self, delta_time):
        self.constructor.scene.update()
        
        # Keep the player on screen
        if self.constructor.player.top > constants.SCREEN_HEIGHT:
            self.constructor.player.top = constants.SCREEN_HEIGHT
        if self.constructor.player.right > constants.SCREEN_WIDTH:
            self.constructor.player.right = constants.SCREEN_WIDTH
        if self.constructor.player.bottom < 0:
            self.constructor.player.bottom = 0
        if self.constructor.player.left < 0:
            self.constructor.player.left = 0
        
        # Collision detection
        if self.constructor.player.collides_with_list(self.constructor.scene.get_sprite_list("Obstacles")):
            arcade.close_window()

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        arcade.start_render()
        # Sets background image
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        
        # Draw all the sprites
        self.constructor.scene.draw()
