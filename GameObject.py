import pygame

from GameManager import GameManager
from Vector2 import Vector2

class GameObject:
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
        if size == None:
            self.size = Vector2(1, 1)
        else:
            self.size = size

        # show gameObject if visible (in renderQueue, of course)
        if self.visible:
            self.show()


    def show(self):
        self.visible = True
        GameManager.addToRenderQueue(self.onRender, self.layer)

    
    def hide(self):
        self.visible = False
        GameManager.removeFromRenderQueue(self.onRender, self.layer)

    # by default, game objects will render self.image in self.position with self.size
    def onRender(self):
        GameManager.screen.blit(self.image, self.position.toArray())