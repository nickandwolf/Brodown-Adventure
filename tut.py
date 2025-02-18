import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Tutorial"

PLAYER_MOVEMENT_SPEED = 5

class GameView(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.player_texture = arcade.load_texture(":resources:/images/enemies/slimeBlock.png")

        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 82

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite)

        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

        arcade.draw_sprite(self.player_sprite)

    def on_update(self, delta_time):
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

def main():
    window = GameView()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()