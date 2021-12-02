import arcade
import arcade.gui
from game import constants

class PauseView(arcade.View):
    
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        """Called when game is paused"""
        arcade.set_background_color(arcade.color.PURPLE)

    def on_draw(self):
        """Called whenever you need to draw your window
        """
        arcade.start_render()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player = self.game_view.constructor.player
        player.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=player.left, right=player.right, top=player.top, bottom=player.bottom, color=arcade.color.PURPLE + (200,))
        
        # Draw text
        arcade.draw_text("PAUSED", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 50, arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press Enter to reset", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 30, arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """Handle user keyboard input
        ESCAPE: Returns to the game
        ENTER: Resets the game

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        
        if key == arcade.key.ESCAPE:   
            # Resume game
            # Resume scheduling of asteroids
            self.game_view.constructor.resume()
            self.window.show_view(self.game_view)
            
        elif key == arcade.key.ENTER:  
            # Reset game
            game_view = self.game_view
            game_view.setup()
            self.window.show_view(game_view)
