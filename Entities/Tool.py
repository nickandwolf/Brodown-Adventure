import Entities.Entity
import Entities.Player

class Tool(Entities.Entity.Entity):
    def __init__(self, x, y, name, description="", sprites = []):
        super().__init__(x, y, name, description)

        self.activeSprite = sprites
        self.carried = False

    def update(self, delta):
        super().update(delta)


    def PickUp(self, player):
        sux = player.pickUpItem(self)
        if sux:
            self.carried = True
        else:
            self.carried = False


    def Drop(self, player):
        sux = player.dropItem(self)
        if sux:
            self.carried = False
        else:
            self.carried = True