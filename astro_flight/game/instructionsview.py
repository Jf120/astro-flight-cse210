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
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.window.set_mouse_visible(True)
        
        # Variable with background image
        self.background = arcade.load_texture("astro_flight/game/images/background.png")
        box = arcade.gui.UIBoxLayout(vertical=False)
        play_button = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('astro_flight/game/images/play.png'), texture_hovered=arcade.load_texture('astro_flight/game/images/play_hovered.png'), texture_pressed=arcade.load_texture('astro_flight/game/images/play_pressed.png'), scale=constants.BUTTON_SCALING)
        box.add(play_button.with_space_around(top=300))
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x='center_x', anchor_y='center_y', child=box))
        play_button.on_click = self.on_click_button_play
        
    
    def on_draw(self):
        """Called whenever you need to draw your window
        """

        arcade.start_render()
        # Sets background image
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        arcade.draw_text("How To Play", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 200, arcade.color.WHITE, font_size=40, anchor_x="center")
        arcade.draw_text("Use AWSD to move", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 350, arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Do not collide with the asteroids", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 400, arcade.color.WHITE, font_size=20, anchor_x="center")
        self.manager.draw()
    
    def on_click(self, event):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
        
    def on_click_button_play(self, event):
        
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
