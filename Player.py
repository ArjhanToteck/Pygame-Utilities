from GameManager import GameManager
from SpriteObject import SpriteObject
from Vector2 import Vector2
import Collider

import pygame

# player class
class Player(SpriteObject):
	def __init__(self, position = None, size = None, visible = True, layer = 1, pivot = None, spritePath = None, sprite = None):
		# do regular sprite init
		super().__init__(position, size, visible, layer, pivot, spritePath, sprite)

		# set speed variable
		self.speed = 5

		# add collider to self		
		Collider.RectangleCollider(parent = self, size = Vector2(1, 1))

	def onUpdate(self):

		# movement
		if GameManager.keysDown[pygame.K_LEFT]:
			self.move(Vector2(-self.speed * GameManager.deltaTime, 0))

		if GameManager.keysDown[pygame.K_RIGHT]:
			self.move(Vector2(self.speed * GameManager.deltaTime, 0))

		if GameManager.keysDown[pygame.K_UP]:
			self.move(Vector2(0, self.speed * GameManager.deltaTime))

		if GameManager.keysDown[pygame.K_DOWN]:
			self.move(Vector2(0, -self.speed * GameManager.deltaTime))