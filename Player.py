from GameManager import GameManager
from Sprite import Sprite
from Vector2 import Vector2
import Collider

import pygame

# player class
class Player(Sprite):
	def __init__(self, position=None, size=None, visible=True, layer=1, pivot = None, imagePath=None, image=None):
		
		# set speed variable
		self.speed = 5

		# add collider to self		
		# player.colliders.append(Collider.Collider(player))

		# do regular sprite init
		super().__init__(position, size, visible, layer, pivot, imagePath, image)


	def onUpdate(self):

		# movement
		if GameManager.keysDown[pygame.K_LEFT]:
			self.move(Vector2(-self.speed * GameManager.deltaTime, 0))
		if GameManager.keysDown[pygame.K_RIGHT]:
			self.move(Vector2(self.speed * GameManager.deltaTime, 0))
		if GameManager.keysDown[pygame.K_UP]:
			self.move(Vector2(0, -self.speed * GameManager.deltaTime))
		if GameManager.keysDown[pygame.K_DOWN]:
			self.move(Vector2(0, self.speed * GameManager.deltaTime))