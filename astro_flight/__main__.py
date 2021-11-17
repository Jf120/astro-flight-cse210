# Imports
import arcade
import arcade.gui
from game import constants
from game.constructor import Constructor

# Classes
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


class HomeView(arcade.View):
    
    def on_show(self):
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        box = arcade.gui.UIBoxLayout(vertical=False)
        play_button = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('astro_flight/game/images/play.png'), texture_hovered=arcade.load_texture('astro_flight/game/images/play_hovered.png'), texture_pressed=arcade.load_texture('astro_flight/game/images/play_pressed.png'), scale=constants.BUTTON_SCALING)
        instructions_button = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('astro_flight/game/images/instructions.png'), texture_hovered=arcade.load_texture('astro_flight/game/images/instructions_hovered.png'), texture_pressed=arcade.load_texture('astro_flight/game/images/instructions_pressed.png'), scale=constants.BUTTON_SCALING)
        box.add(play_button.with_space_around(bottom=20))
        box.add(instructions_button.with_space_around(bottom=20))
        play_button.on_click = self.on_click_button
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x='center_x', anchor_y='center_y', child=box))
        
        # Variable with background image
        self.background = arcade.load_texture("astro_flight/game/images/background.png")
            
    def on_draw(self):
        
        """Called whenever you need to draw your window
        """

        arcade.start_render()
        # Sets background image
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        self.manager.draw()

    def on_click_button(self, event):
        
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
        
# Main code entry point
if __name__ == "__main__":
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = HomeView()
    window.show_view(start_view)
    arcade.run()