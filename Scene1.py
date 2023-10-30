from GameManager import GameManager
from GameObject import GameObject
from Sprite import Sprite
from Vector2 import Vector2

import pygame

# this class contains all the game objects and stuff it needs
class Scene1:

    @staticmethod
    def start():
        background = Scene1.Background()
        player = Scene1.Player(imagePath = "test.png")


    class Background(GameObject):
        def onRender(self):
            # clear game
            GameManager.screen.fill("black")


    class Player(Sprite):
        def onUpdate(self):
            if GameManager.keysDown[pygame.K_LEFT]:
                self.position.x -= GameManager.deltaTime
            if GameManager.keysDown[pygame.K_RIGHT]:
                self.position.x += GameManager.deltaTime
            if GameManager.keysDown[pygame.K_UP]:
                self.position.y -= GameManager.deltaTime
            if GameManager.keysDown[pygame.K_DOWN]:
                self.position.y += GameManager.deltaTime