import arcade

class Entity:
    def __init__(self, x, y, name, description="", MOVEMENT_SPEED = 1, SPRITE_SCALE = 1, sprites=[], action=None):
        self.x = x
        self.y = y
        self.spriteList = arcade.SpriteList()

        self.SPRITE_SCALE = SPRITE_SCALE
        self.MOVEMENT_SPEED = MOVEMENT_SPEED

        for x in sprites:
            self.spriteList.append(arcade.Sprite(x, self.SPRITE_SCALE))

        self.name = name
        self.description = description
        self.action = action

        self.activeSprite = 0
        if len(self.spriteList) > 0:
            self.activeSprite = self.spriteList[0]
            self.activeSprite.center_x = self.x
            self.activeSprite.center_y = self.y

    def getCollisionList(self, other):
        return arcade.check_for_collision_with_list(self.spriteList, other)
    
    def getCollision(self, other):#TODO: probably not needed
        hits = arcade.check_for_collision_with_list(self.spriteList, other)
        if len(hits) > 0:
            return True
        return False

    def setSpriteScale(self, scale):
        self.SPRITE_SCALE = scale

    def addSprite(self, sprite, scale=None):
        if scale == None:
            scale = self.SPRITE_SCALE
        self.spriteList.append(arcade.Sprite(sprite, scale))

    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def move(self, dx, dy):
        self.activeSprite.change_x = dx
        self.activeSprite.change_y = dy

    def setPos(self, x, y):
        self.activeSprite.center_x = x
        self.activeSprite.center_y = y

    def getPos(self):
        return self.activeSprite.position
    
    def getX(self):
        return self.activeSprite.center_x
    
    def getY(self):
        return self.activeSprite.center_y

    def draw(self):
        arcade.draw_sprite(self.activeSprite)

    def update(self, delta):
        self.spriteList.update(delta)