import pygame

from GameManager import GameManager
from Vector2 import Vector2
from GameObject import GameObject

# sprites are a template for GameObjects that rely on a 2d image
class Sprite(GameObject):
	def __init__(self, position = None, size = None, visible = True, layer = 1, pivot = None, imagePath = None, image = None):
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
			# set size based on image
			if self.image != None:
				self.setSizePixels(Vector2(self.image.get_width(), self.image.get_height()))
			else:
				self.setSize(Vector2(1, 1))
		else:
			self.setSize(size)

		# set default for pivot (distance from center in percentage of total size)
		if pivot == None:
			self.pivot = Vector2(0, 0)
		else:
			self.pivot = pivot

		# do the regular __init__ for gameObjects
		super().__init__(visible, layer)


	def setSize(self, size):
		self.size = size
		self.image = pygame.transform.scale(self.image, (self.size * GameManager.worldUnitSize).toArray())


	def setSizePixels(self, size):
		self.setSize(size / GameManager.worldUnitSize)


	def scale(self, factor):
		self.setSize(self.size * factor)


	def move(self, movement):
		self.position += movement

		# TODO: implement collisions here


	def setPosition(self, position):
		self.position = position

	
	def setPositionInPixels(self, position):
		self.setPosition(position / GameManager.worldUnitSize)


	def setImage(self, image):
		self.image = pygame.image.load(image)


	def setImageFromPath(self, imagePath):
		self.image = pygame.image.load(imagePath)


	# by default, game objects will render self.image in self.position with self.size
	def onRender(self):
		# get screen position of sprite (top left corner)
		screenPosition = GameManager.worldToScreenPosition(self.position)

		# center of sprite (default pivot)
		pivotOffset = (self.size / 2) * GameManager.worldUnitSize

		# invert y of pivot
		pivotYInverted = self.pivot.clone()
		pivotYInverted.y *= -1

		# add pivot to offset (percentage of size)
		pivotOffset += pivotYInverted * (self.size / 2) * GameManager.worldUnitSize

		# add 
		screenPosition -= pivotOffset

		# draw image at position
		GameManager.screen.blit(self.image, screenPosition.toArray())