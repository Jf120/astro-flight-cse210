import arcade
import arcade.gui
import constants

class Home(arcade.Window):
    
    def __init__(self):
        """Initialize the window
        """
        
        # Sets size of the window and title
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        
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
    @staticmethod
    def on_click_button(event):
        print('Button clicked!')
    
    def on_draw(self):
        """Called whenever you need to draw your window
        """

        arcade.start_render()
        # Sets background image
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        self.manager.draw()
    
# Main code entry point
if __name__ == "__main__":
    app = Home()
    arcade.run()