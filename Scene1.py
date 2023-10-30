from GameManager import GameManager
from GameObject import GameObject
from Sprite import Sprite
from Vector2 import Vector2
import Collider

import pygame

# this class contains all the game objects and stuff for the scene
class Scene1:

	# this is called when the scene is opened. creates all the gameObjects it needs.
	@staticmethod
	def start():
		background = Scene1.Background()
		player = Scene1.Player(imagePath = "test.png")
		player.colliders.append(Collider.Collider(player))


	# background class
	class Background(GameObject):
		def onRender(self):
			# clear game
			GameManager.screen.fill("black")


	# player class
	class Player(Sprite):
		def __init__(self, position=None, size=None, visible=True, layer=1, imagePath=None, image=None):
			self.speed = 5

			# do regular sprite init
			super().__init__(position, size, visible, layer, imagePath, image)


		def onUpdate(self):

			# movement
			if GameManager.keysDown[pygame.K_LEFT]:
				self.position.x -= self.speed * GameManager.deltaTime
			if GameManager.keysDown[pygame.K_RIGHT]:
				self.position.x += self.speed * GameManager.deltaTime
			if GameManager.keysDown[pygame.K_UP]:
				self.position.y -= self.speed * GameManager.deltaTime
			if GameManager.keysDown[pygame.K_DOWN]:
				self.position.y += self.speed * GameManager.deltaTime