import arcade
import arcade.gui
from game import constants
from game.gameview import GameView

class InstructionsView(arcade.View):
    """Instructions window
    """
    def __init__(self):
        """Initialize the window
        """
        
        # Sets size of the window and title
        super().__init__()
        
        # Adds manager for buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Mouse visibility
        self.window.set_mouse_visible(True)
        
        # Variable with background image
        self.background = arcade.load_texture(constants.PATH + "/images/background.png")
        
        # Creates box with button
        box = arcade.gui.UIBoxLayout(vertical=False)
        play_button = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture(constants.PATH + '/images/play.png'), texture_hovered=arcade.load_texture(constants.PATH + '/images/play_hovered.png'), texture_pressed=arcade.load_texture(constants.PATH + '/images/play_pressed.png'), scale=constants.BUTTON_SCALING)
        
        # Adds on_click action to play button
        play_button.on_click = self.on_click_button_play
        
        # Adds button to box
        box.add(play_button.with_space_around(top=300))
        
        # Adds box to manager
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x='center_x', anchor_y='center_y', child=box))
        
    def on_draw(self):
        """Called whenever you need to draw your window
        """
        # Starts the render
        arcade.start_render()
        
        # Sets background image
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        
        # Adds text to the window
        arcade.draw_text("How To Play", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 200, arcade.color.WHITE, font_size=40, anchor_x="center")
        arcade.draw_text("Use AWSD to move", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 350, arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Do not collide with the asteroids", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 400, arcade.color.WHITE, font_size=20, anchor_x="center")
        
        # Draws the manager (buttons)
        self.manager.draw()
        
    def on_click_button_play(self, event):
        """ If the user presses play button, start the game. 
        """
        
        # Loads and launches GameView
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
