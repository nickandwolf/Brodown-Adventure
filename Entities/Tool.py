import Entities.Entity

class Tool(Entities.Entity.Entity):
    def __init__(self, x, y, name, description="", sprites = []):
        super().__init__(x, y, name, description)

        self.activeSprite = sprites
        self.carried = False

    def update(self, delta):
        pass