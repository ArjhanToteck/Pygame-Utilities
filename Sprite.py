import pygame

from GameManager import GameManager
from Vector2 import Vector2
from GameObject import GameObject

# sprites are a template for GameObjects that rely on a 2d image
class Sprite(GameObject):
    def __init__(self, position = None, size = None, visible = True, layer = 1, imagePath = None, image = None):
        self.image = image
        self.layer = layer

        # while this can be set at instantiation, helper functions should be used to hide and show the object afterwards
        self.visible = visible

        # set default for image with path
        if imagePath != None:
            self.image = pygame.image.load(imagePath)

        # set default for position (world units)
        if position == None:
            self.position = Vector2(0, 0)
        else:
            self.position = position
        
        # set default for size (world units)
        # while this can be set at instantiation, helper functions should be used to set the size of the object afterwards
        if size == None:
            self.setSize(Vector2(1, 1))
        else:
            self.setSize(size)

        # show gameObject if visible (in renderQueue, of course)
        if self.visible:
            self.show()

        # track gameObject in GameManager
        GameManager.gameObjects.append(self)


    def setSize(self, size):
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size * GameManager.worldUnitSize).toArray())


    # by default, game objects will render self.image in self.position with self.size
    def onRender(self):
        GameManager.screen.blit(self.image, (self.position * GameManager.worldUnitSize).toArray())