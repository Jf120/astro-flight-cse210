import arcade
import arcade.gui
from game import constants

class InstructionsView(arcade.View):
    """Instructions window
    """
    def __init__(self, home_view):
        """Initialize the window
        """
        
        # Sets size of the window and title
        super().__init__()
        
        # sets home_view to go back
        self.home_view = home_view
        
        # Adds manager for buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Mouse visibility
        self.window.set_mouse_visible(True)
        
        # Variable with background image
        self.background = arcade.load_texture(constants.PATH + "/images/background.png")
        
        # Creates box with button
        box = arcade.gui.UIBoxLayout(vertical=False)
        back_button = arcade.gui.UITextureButton(texture=arcade.load_texture(constants.PATH + '/images/back.png'), texture_hovered=arcade.load_texture(constants.PATH + '/images/back_pressed.png'), texture_pressed=arcade.load_texture(constants.PATH + '/images/back_pressed.png'), scale=constants.BUTTON_SCALING)
        
        # Adds on_click action to play button
        back_button.on_click = self.on_click_button_back
        
        # Adds button to box
        box.add(back_button.with_space_around(top=300))
        
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
        arcade.draw_text("How To Play", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 200, arcade.color.WHITE, font_size=40, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("Use AWSD to move", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 350, arcade.color.WHITE, font_size=16, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("Do not collide with the asteroids", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 400, arcade.color.WHITE, font_size=16, anchor_x="center", font_name="Kenney Future")
        
        # Draws the manager (buttons)
        self.manager.draw()
        
    def on_click_button_back(self, event):
        """ If the user presses the back button, go back to the home screen
        """
        
        # Launches homeview
        self.window.show_view(self.home_view)
