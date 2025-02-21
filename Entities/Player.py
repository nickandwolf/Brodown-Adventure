import Entities.Entity
#import arcade
from universalVariables import *

class Player(Entities.Entity.Entity):
    def __init__(self, x, y, name, sprites=[], SPRITE_SCALE = 1):
        super().__init__(x, y, name, "This is the player", 2, SPRITE_SCALE, sprites)

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def move(self):
        self.activeSprite.change_x = 0
        self.activeSprite.change_y = 0

        if self.move_up and not self.move_down:
            self.activeSprite.change_y = self.MOVEMENT_SPEED
        elif self.move_down and not self.move_up:
            self.activeSprite.change_y = -self.MOVEMENT_SPEED
        if self.move_left and not self.move_right:
            self.activeSprite.change_x = -self.MOVEMENT_SPEED
        elif self.move_right and not self.move_left:
            self.activeSprite.change_x = self.MOVEMENT_SPEED

    def handleKeyPress(self, key, modifiers):
        if key == key_bindings["move_up"]:
            self.move_up = True
            self.move()
        elif key == key_bindings["move_down"]:
            self.move_down = True
            self.move()
        elif key == key_bindings["move_left"]:
            self.move_left = True
            self.move()
        elif key == key_bindings["move_right"]:
            self.move_right = True
            self.move()

    def handleKeyRelease(self, key, modifiers):
        if key == key_bindings["move_up"]:
            self.move_up = False
            self.move()
        elif key == key_bindings["move_down"]:
            self.move_down = False
            self.move()
        elif key == key_bindings["move_left"]:
            self.move_left = False
            self.move()
        elif key == key_bindings["move_right"]:
            self.move_right = False
            self.move()

    def update(self, delta):
        if self.activeSprite.left < 0:
            self.activeSprite.left = 0
        elif self.activeSprite.right > WINDOW_WIDTH-1:
            self.activeSprite.right = WINDOW_WIDTH-1
        
        if self.activeSprite.bottom < 0:
            self.activeSprite.bottom = 0
        elif self.activeSprite.top > WINDOW_HEIGHT-1:
            self.activeSprite.top = WINDOW_HEIGHT-1