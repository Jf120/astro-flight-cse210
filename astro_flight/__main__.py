# Imports
import arcade
import arcade.gui
from game import constants
from game.gameview import GameView
from game.instructionsview import InstructionsView

# Home View Class
class HomeView(arcade.View):
    
    def on_show(self):
        
        # Sets Manager for GUI
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        # Adds play and instructions buttons
        box = arcade.gui.UIBoxLayout(vertical=False)
        play_button = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture(constants.PATH + '/images/play.png'), texture_hovered=arcade.load_texture(constants.PATH + '/images/play_hovered.png'), texture_pressed=arcade.load_texture(constants.PATH + '/images/play_pressed.png'), scale=constants.BUTTON_SCALING)
        instructions_button = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture(constants.PATH + '/images/instructions.png'), texture_hovered=arcade.load_texture(constants.PATH + '/images/instructions_hovered.png'), texture_pressed=arcade.load_texture(constants.PATH + '/images/instructions_pressed.png'), scale=constants.BUTTON_SCALING)
        box.add(play_button.with_space_around(bottom=20))
        box.add(instructions_button.with_space_around(bottom=20))
        play_button.on_click = self.on_click_button_play
        instructions_button.on_click = self.on_click_button_instructions
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x='center_x', anchor_y='center_y', child=box))
        
        # Variable with background image
        self.background = arcade.load_texture(constants.PATH + "/images/background.png")
        self.background_music = arcade.load_sound(constants.PATH + "/sounds/background_music.wav")
        # Starts music
        arcade.play_sound(self.background_music, 0.6, 0, True)
            
    def on_draw(self):
        
        """Called whenever you need to draw your window
        """

        arcade.start_render()
        # Sets background image
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        # Draws buttons
        self.manager.draw()

    def on_click_button_play(self, event):
        
        # If button clicked the launches game
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
    
    def on_click_button_instructions(self, event):
        
        # If button clicked then the launches instructions
        instructions_view = InstructionsView()
        self.window.show_view(instructions_view)

        
# Main code entry point
if __name__ == "__main__":
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = HomeView()
    window.show_view(start_view)
    arcade.run()