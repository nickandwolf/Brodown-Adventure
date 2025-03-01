import arcade
import Entities.Player
from settings.universalVariables import *
from arcade.types import LRBT
from AudioHandler import *

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_FULLSCREEN, draw_rate=WINDOW_FPS)
        self.center_window()
        self.camera = arcade.camera.Camera2D(position=(0, 0),
            projection=LRBT(left=0, right=GAME_WIDTH, bottom=0, top=GAME_HEIGHT))
        
        scale_factor = self.height / GAME_HEIGHT
        new_width = GAME_WIDTH * scale_factor
        margin = (self.width - new_width) / 2
        self.camera.viewport = LRBT(margin, self.width - margin, 0, self.height)
        
    def on_key_press(self, key, modifiers):
        if key == key_bindings["fullscreen"]:
            self.set_fullscreen(not self.fullscreen)
            self.camera.projection = LRBT(left=0, right=GAME_WIDTH,
                                        bottom=0, top=GAME_HEIGHT)
            
            screen_ratio = self.width / self.height
            game_ratio = GAME_WIDTH / GAME_HEIGHT

            if screen_ratio > game_ratio:
                scale_factor = self.height / GAME_HEIGHT
                new_width = GAME_WIDTH * scale_factor
                margin = (self.width - new_width) / 2
                self.camera.viewport = LRBT(margin, self.width - margin, 0, self.height)

            else:
                self.camera.viewport = self.rect

    def on_draw(self):
        self.camera.use()
        arcade.draw_rect_outline(LRBT(0, 800, 0, 600),
            color=arcade.color.WHITE, border_width=5)
        
class DevIntroScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.pointer = 0
        self.window.background_color = arcade.csscolor.BLACK
        
        self.song = arcade.Sound("./Sound/freaky.mp3", True)
        self.music_player = self.song.play(MUSIC_VOLUME)


        self.img = arcade.Sprite(arcade.load_texture("./Graphics/splashscreen/freak!.jpg"), 0.5)
        self.img.center_x = self.img.width / 2 + GAME_WIDTH / 4
        self.img.center_y = self.img.height / 2 + 40
        self.img.alpha = 0

    def on_key_press(self, symbol, modifiers):
        self.finalScreen()

    def on_draw(self):
        self.clear()
        with self.window.camera.activate():
            arcade.draw_sprite(self.img)

    def on_update(self, delta):
        self.timer += delta
        if self.timer < 1:
            if self.img.alpha < 255:
                self.img.alpha += 10
            else:
                self.img.alpha = 255
        if self.timer > 2.3:
            self.img.alpha -=15
        if self.timer > 3:
            self.finalScreen()
        

    def finalScreen(self):
        next_screen = IntroStoryScreen()
        self.window.show_view(next_screen)
        self.music_player.delete()
        del self

class IntroStoryScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.pointer = 0
        self.window.background_color = arcade.csscolor.BLACK
        
        self.top_text = arcade.Text(" ", 0, 0)
        self.bottom_text = arcade.Text(" ", 0, 0)
        self.song = arcade.Sound("./Music/Intro.wav", True)
        self.music_player = self.song.play(MUSIC_VOLUME)

        self.screen1()
        
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
            self.screen1()
        elif self.pointer == 1:
            self.screen2()
        elif self.pointer == 2:
            self.screen3()
        elif self.pointer > 2:
            self.finalScreen()
            
    def on_key_press(self, symbol, modifiers):
        self.pointer +=1

    def finalScreen(self):
        next_screen = TitleScreen()
        self.window.show_view(next_screen)
        self.music_player.delete()
        del self

    def screen1(self):
        self.top_text = arcade.Text("The Story of the Game",
                            x=GAME_WIDTH / 2, y=GAME_HEIGHT / 2,
                            color=arcade.color.WHITE, font_size=50,
                            anchor_x="center")

        self.bottom_text = arcade.Text("Once upon a time...",
                                x=GAME_WIDTH / 2, y=GAME_HEIGHT / 2-75,
                                color=arcade.color.WHITE, font_size=20,
                                anchor_x="center")
        
    def screen2(self):
        self.top_text = arcade.Text("2nd screen shows up",
                            x=GAME_WIDTH / 2, y=GAME_HEIGHT / 2,
                            color=arcade.color.WHITE, font_size=50,
                            anchor_x="center")

        self.bottom_text = arcade.Text("with more text...",
                                x=GAME_WIDTH / 2, y=GAME_HEIGHT / 2-75,
                                color=arcade.color.WHITE, font_size=20,
                                anchor_x="center")
        
    def screen3(self):
        self.top_text = arcade.Text("final screen",
                            x=GAME_WIDTH / 2, y=GAME_HEIGHT / 2,
                            color=arcade.color.WHITE, font_size=50,
                            anchor_x="center")

        self.bottom_text = arcade.Text("and we prep for the title screen...",
                                x=GAME_WIDTH / 2, y=GAME_HEIGHT / 2-75,
                                color=arcade.color.WHITE, font_size=20,
                                anchor_x="center")

class TitleScreen(arcade.View):
    def __init__(self):
        super().__init__()

        self.window.background_color = arcade.csscolor.DARK_SLATE_GREY
        self.title_text = arcade.Text("Brodown Adventure",
                            x=GAME_WIDTH / 2, y=GAME_HEIGHT / 2,
                            color=arcade.color.WHITE, font_size=50,
                            anchor_x="center")

        self.instruction_text = arcade.Text("Press anykey to start (no options yet)",
                                x=GAME_WIDTH / 2, y=GAME_HEIGHT / 2-75,
                                color=arcade.color.WHITE, font_size=20,
                                anchor_x="center")
        
        self.song = arcade.Sound("./Music/Title.mp3", True)
        self.music_player = self.song.play(MUSIC_VOLUME)

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

    def __init__(self, playerX = 392, playerY = 292):
        """ We only need to set where the player enters the screen by default. """
        super().__init__()
        self.Player = Entities.Player.Player(playerX, playerY)

        self.audio = AudioHandler([arcade.Sound("./Music/Level1.mp3")])
        self.audio.setLoop(0, True)
        self.audio.playMusic(0)

        self.level = arcade.load_tilemap("./Tiled/level1.tmx", 5)
        self.walls = self.level.sprite_lists["walls"]
        self.pickaxe = self.level.sprite_lists["pickaxe"]

        self.physics_engine = arcade.PhysicsEngineSimple(self.Player.activeSprite, self.walls)

        if self.level.background_color:
            self.window.background_color = self.level.background_color
        
        else:
            arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)


    def on_draw(self):
        self.clear()
        with self.window.camera.activate():
            self.walls.draw(pixelated=True)
            self.Player.draw()

    def on_update(self, delta):
        self.physics_engine.update()
        self.walls.update()
        self.Player.update(delta)

    def on_key_press(self, key, modifiers):
        self.Player.handleKeyPress(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.Player.handleKeyRelease(key, modifiers)

def main():
    window = GameWindow()
    #window.show_view(DevIntroScreen())
    window.show_view(GameView())
    arcade.run()

if __name__ == "__main__":
    main()
 