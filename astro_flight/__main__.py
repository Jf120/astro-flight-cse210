# Imports
import arcade
import arcade.gui
from game import constants
from game.gameview import GameView
from game.instructionsview import InstructionsView

# Home View Class
class HomeView(arcade.View):
    """Initialize Home window
    """
    
    def __init__(self):
        super().__init__()
        # Variable with background image
        self.background = arcade.load_texture(constants.PATH + "/images/background_logo.png")
        
        # Loads and plays music
        self.music = arcade.load_sound(constants.PATH + "/sounds/music.wav", streaming = True)
        arcade.play_sound(self.music, 0.5, looping = True)\
        
        # Sets Manager for GUI
        self.manager = arcade.gui.UIManager()
        self.manager.enable() 
        
    def setup(self):
        """Called when the view is shown
        """
        
        # Adds play and instructions buttons
        box = arcade.gui.UIBoxLayout(vertical=False)
        play_button = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture(constants.PATH + '/images/play.png'), texture_hovered=arcade.load_texture(constants.PATH + '/images/play_hovered.png'), texture_pressed=arcade.load_texture(constants.PATH + '/images/play_pressed.png'), scale=constants.BUTTON_SCALING)
        instructions_button = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture(constants.PATH + '/images/instructions.png'), texture_hovered=arcade.load_texture(constants.PATH + '/images/instructions_hovered.png'), texture_pressed=arcade.load_texture(constants.PATH + '/images/instructions_pressed.png'), scale=constants.BUTTON_SCALING)
        box.add(play_button.with_space_around(top=200))
        box.add(instructions_button.with_space_around(top=200))
        play_button.on_click = self.on_click_button_play
        instructions_button.on_click = self.on_click_button_instructions
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x='center_x', anchor_y='center_y', child=box))
        
    def on_draw(self):
        
        """Called whenever you need to draw your window
        """

        arcade.start_render()
        # Sets background image
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        # Draws buttons
        self.manager.draw()

    def on_click_button_play(self, event):
        """Called whenever you click the play button
        """
        
        # If button clicked the launches game
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
    
    def on_click_button_instructions(self, event):
        """Called whenever you click the instructions button
        """
        
        # If button clicked then the launches instructions
        instructions_view = InstructionsView(self)
        self.window.show_view(instructions_view)

        
# Main code entry point
if __name__ == "__main__":
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = HomeView()
    start_view.setup()
    window.show_view(start_view)
    arcade.run()