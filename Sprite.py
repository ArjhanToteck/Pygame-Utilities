import pygame

from GameManager import GameManager
from Vector2 import Vector2
from GameObject import GameObject

# sprites are a template for GameObjects that rely on a 2d image
class Sprite(GameObject):
	def __init__(self, position = None, size = None, visible = True, layer = 1, imagePath = None, image = None):
		self.image = image

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

		# do the regular __init__ for gameObjects
		super().__init__(visible, layer)


	def setSize(self, size):
		self.size = size
		self.image = pygame.transform.scale(self.image, (self.size * GameManager.worldUnitSize).toArray())


	def setImage(self, image):
		self.image = pygame.image.load(image)


	def setImageFromPath(self, imagePath):
		self.image = pygame.image.load(imagePath)


	# by default, game objects will render self.image in self.position with self.size
	def onRender(self):
		GameManager.screen.blit(self.image, (self.position * GameManager.worldUnitSize).toArray())