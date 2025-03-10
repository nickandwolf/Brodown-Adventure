import Entities.Entity
from settings.universalVariables import *
from arcade.types import LRBT

class Player(Entities.Entity.Entity):
    def __init__(self, x, y, name="Player", sprites=["./Graphics/basictiles.png"], SPRITE_SCALE = [5,5], inventory = []):
        super().__init__(x, y, name, "This is the player", 3, SPRITE_SCALE, sprites, sprite_sheet=True)

        self.ANIMATION_SPEED = 0.63157
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.inventory = []

        # 0 = up
        # 1 = right
        # 2 = down
        # 3 = left
        self.rotation = 0

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
        elif key == key_bindings["rotate_left"]:
            self.rotation -= 1
            if rotation < 0:
                rotation = 3
        elif key == key_bindings["rotate_right"]:
            self.rotation += 1
            if rotation > 3:
                rotation = 0
        elif key == key_bindings["action"]:
            pass


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
        super().update(delta)
        if self.activeSprite.left < 0:
            self.activeSprite.left = 0
        elif self.activeSprite.right > GAME_WIDTH-1:
            self.activeSprite.right = GAME_WIDTH-1
        
        if self.activeSprite.bottom < 0:
            self.activeSprite.bottom = 0
        elif self.activeSprite.top > GAME_HEIGHT-1:
            self.activeSprite.top = GAME_HEIGHT-1

    def pickUpItem(self, item):
        if len(self.inventory < 4):
            self.inventory.append(item)
            return True
        return False

    def dropItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False