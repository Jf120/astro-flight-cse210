import arcade
import arcade.gui
from game import constants

class GameOverView(arcade.View):
    
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        
        # Variable with background image
        self.background = arcade.load_texture("astro_flight/game/images/background.png")
        
        # Mouse visibility
        self.window.set_mouse_visible(True)
    
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    
    def on_draw(self):
        """Draws the window
        """
        # Starts render
        arcade.start_render()
        
        # Draw the background and text
        arcade.draw_texture_rectangle(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        arcade.draw_text("You Lost!", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 200, arcade.color.WHITE, font_size=40, anchor_x="center")
        arcade.draw_text("Press 'Q' to quit", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 350, arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Press ENTER to restart", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 500, arcade.color.WHITE, font_size=20, anchor_x="center")    
        
    def on_key_press(self, key, _modifiers):
        """Handle user keyboard input
        R: Restarts the game
        Q: Quit the game

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        
        # Restarts the game if R is pressed
        if key == arcade.key.ENTER:
            
            game_view = self.game_view
            game_view.setup()
            self.window.show_view(self.game_view)
            
        # Quits the game if Q is pressed
        elif key == arcade.key.Q:
            self.window.close()