import arcade
import Entities.Player
from settings.universalVariables import *

class GameView(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.Player = Entities.Player.Player(10, 10, "Player", [arcade.load_texture(":resources:/images/enemies/slimeBlock.png")])
        self.Player.activeSprite.center_x = 100
        self.Player.activeSprite.center_y = 100
        self.physics_engine = arcade.PhysicsEngineSimple(self.Player.activeSprite)

        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

        self.Player.draw()

    def on_update(self, delta_time):
        self.Player.update(delta_time)
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        self.Player.handleKeyPress(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.Player.handleKeyRelease(key, modifiers)

def main():
    window = GameView()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
