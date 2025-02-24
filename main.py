import arcade
import Entities.Player
from settings.universalVariables import *
from arcade.types import LRBT

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_FULLSCREEN)
        self.center_window()
        self.camera = arcade.camera.Camera2D(position=(0, 0),
            projection=LRBT(left=0, right=WINDOW_WIDTH, bottom=0, top=WINDOW_HEIGHT),
            viewport=self.rect)
        self.camera.use()

    def on_key_press(self, key, modifiers):
        if key == key_bindings["fullscreen"]:
            self.set_fullscreen(not self.fullscreen)
            self.camera.projection = LRBT(left=0, right=WINDOW_WIDTH,
                                        bottom=0, top=WINDOW_HEIGHT)
            self.camera.viewport = self.rect
        

class IntroStoryScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.pointer = 0
        self.window.background_color = arcade.csscolor.BLACK
        
        self.music_player = arcade.Sound("./Music/Intro.wav", True).play()

        self.screen0()
        
    def on_draw(self):
        self.clear()
        with self.window.camera.activate():
            self.top_text.draw()
            self.bottom_text.draw()

    def on_update(self, delta):
        self.timer += delta
        if self.timer > 5:
            self.timer = 0
            self.pointer += 1

        if self.pointer == 0:
            self.screen0()
        elif self.pointer == 1:
            self.screen1()
        elif self.pointer == 2:
            self.screen2()
        elif self.pointer == 3:
            self.screen3()
        elif self.pointer > 3:
            self.finalScreen()
            
    def on_key_press(self, symbol, modifiers):
        self.pointer +=1

    def finalScreen(self):
        next_screen = TitleScreen()
        self.window.show_view(next_screen)
        self.music_player.delete()
        del self

    def screen0(self):
        self.top_text = arcade.Text("Created by:",
                            x=self.window.width / 2, y=self.window.height / 2,
                            color=arcade.color.WHITE, font_size=50,
                            anchor_x="center")

        self.bottom_text = arcade.Text("Nelson, Nelson, and Nelson",
                                x=self.window.width / 2, y=self.window.height / 2-75,
                                color=arcade.color.WHITE, font_size=20,
                                anchor_x="center")

    def screen1(self):
        self.top_text = arcade.Text("The Story of the Game",
                            x=self.window.width / 2, y=self.window.height / 2,
                            color=arcade.color.WHITE, font_size=50,
                            anchor_x="center")

        self.bottom_text = arcade.Text("Once upon a time...",
                                x=self.window.width / 2, y=self.window.height / 2-75,
                                color=arcade.color.WHITE, font_size=20,
                                anchor_x="center")
        
    def screen2(self):
        self.top_text = arcade.Text("2nd screen shows up",
                            x=self.window.width / 2, y=self.window.height / 2,
                            color=arcade.color.WHITE, font_size=50,
                            anchor_x="center")

        self.bottom_text = arcade.Text("with more text...",
                                x=self.window.width / 2, y=self.window.height / 2-75,
                                color=arcade.color.WHITE, font_size=20,
                                anchor_x="center")
        
    def screen3(self):
        self.top_text = arcade.Text("final screen",
                            x=self.window.width / 2, y=self.window.height / 2,
                            color=arcade.color.WHITE, font_size=50,
                            anchor_x="center")

        self.bottom_text = arcade.Text("and we prep for the title screen...",
                                x=self.window.width / 2, y=self.window.height / 2-75,
                                color=arcade.color.WHITE, font_size=20,
                                anchor_x="center")

class TitleScreen(arcade.View):
    def __init__(self):
        super().__init__()

        self.window.background_color = arcade.csscolor.AQUAMARINE
        self.title_text = arcade.Text("Brodown Adventure",
                            x=self.window.width / 2, y=self.window.height / 2,
                            color=arcade.color.WHITE, font_size=50,
                            anchor_x="center")

        self.instruction_text = arcade.Text("Press anykey to start (no options yet)",
                                x=self.window.width / 2, y=self.window.height / 2-75,
                                color=arcade.color.WHITE, font_size=20,
                                anchor_x="center")
        
        self.music_player = arcade.Sound("./Music/Title.mp3", True).play()

    def on_draw(self):
        self.clear()
        with self.window.camera.activate():
            self.title_text.draw()
            self.instruction_text.draw()

    def on_key_press(self, symbol, modifiers):
        next_screen = GameView()
        self.window.show_view(next_screen)
        self.music_player.delete()
        self.music_player = None
        del self

class GameView(arcade.View):
    """ This is the skeleton for creating all game screens. """

    def __init__(self, playerX = 0, playerY = 0):
        """ We only need to set where the player enters the screen by default. """
        super().__init__()
        self.Player = Entities.Player.Player(playerX, playerY, "Player", [arcade.load_texture(":resources:/images/enemies/slimeBlock.png")])
        self.physics_engine = arcade.PhysicsEngineSimple(self.Player.activeSprite)
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

        self.music_player = arcade.Sound("./Music/Level1.mp3", streaming=True).play()
        self.music_player.loop = True

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        with self.window.camera.activate():
            self.Player.draw()

    def on_update(self, delta_time):
        self.Player.update(delta_time)
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        self.Player.handleKeyPress(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.Player.handleKeyRelease(key, modifiers)

def main():
    window = GameWindow()
    window.show_view(IntroStoryScreen())
    arcade.run()

if __name__ == "__main__":
    main()
