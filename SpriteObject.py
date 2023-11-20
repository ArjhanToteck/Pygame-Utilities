from shutil import move
import pygame

from GameManager import GameManager
from Vector2 import Vector2
from Vector2Bool import Vector2Bool
from GameObject import GameObject

# sprites are a template for GameObjects that rely on a 2d image
class SpriteObject(GameObject):
	def __init__(self, position = None, size = None, visible = True, layer = 1, reflection = None, pivot = None, spritePath = None, sprite = None):
		# do the regular __init__ for gameObjects
		super().__init__(visible, layer)

		self.sprite = sprite

		# set default for sprite with path
		if spritePath != None:
			self.sprite = pygame.image.load(spritePath)
			
		# set default for position (world units)
		if position == None:
			self.position = Vector2(0, 0)
		else:
			self.position = position

		# set default for reflection
		if reflection == None:
			self.reflection = Vector2Bool(False, False)
		else:
			self.reflection = reflection
		
		# set default for size (world units)
		# while this can be set at instantiation, helper functions should be used to set the size of the object afterwards
		if size == None:
			# set size based on sprite
			if self.sprite != None:
				self.setSizePixels(Vector2(self.sprite.get_width(), self.sprite.get_height()))
			else:
				self.setSize(Vector2(1, 1))
		else:
			self.setSize(size)

		# set default for pivot (distance from center in percentage of total size)
		if pivot == None:
			self.pivot = Vector2(0, 0)
		else:
			self.pivot = pivot


	def setSize(self, size):
		self.size = size
		self.sprite = pygame.transform.scale(self.sprite, (self.size * GameManager.worldUnitSize).toArray())


	def setSizePixels(self, size):
		self.setSize(size / GameManager.worldUnitSize)


	def scale(self, factor):
		self.setSize(self.size * factor)


	def move(self, movement):
		# remember original position in case of collision
		originalPosition = self.position.clone()

		# update position
		self.position += movement

		permittedPosition = self.position

		for collider in self.colliders:
			currentPermittedPosition = collider.requestMovement(originalPosition, self.position)

			# set permittedPosition to currentPermitedPosition
			if Vector2.distance(currentPermittedPosition, originalPosition) < Vector2.distance(permittedPosition, originalPosition):
				permittedPosition = currentPermittedPosition

		# move to the permitted position
		self.position = permittedPosition

		for collider in self.colliders:
			if collider.followParent:
				collider.position = self.position


	def setPosition(self, position):
		self.position = position

	
	def setPositionInPixels(self, position):
		self.setPosition(position / GameManager.worldUnitSize)


	def setSprite(self, sprite):
		self.sprite = sprite


	def setSpriteFromPath(self, spritePath):
		self.sprite = pygame.image.load(spritePath)


	# by default, game objects will render self.sprite in self.position with self.size
	def onRender(self):
		if self.visible:
			# get screen position of sprite (top left corner)
			screenPosition = GameManager.worldToScreenPosition(self.position)

			# center of sprite (default pivot)
			pivotOffset = (self.size / 2) * GameManager.worldUnitSize

			# invert y of pivot
			pivotYInverted = self.pivot.clone()
			pivotYInverted.y *= -1

			# add pivot to offset (percentage of size)
			pivotOffset += pivotYInverted * (self.size / 2) * GameManager.worldUnitSize

			# subtract pivot
			screenPosition -= pivotOffset

			# reflect sprite
			reflectedSprite = pygame.transform.flip(self.sprite, self.reflection.x, self.reflection.y)

			# draw sprite at position
			GameManager.screen.blit(reflectedSprite, screenPosition.toArray())

		# perform normal gameObject render
		super().onRender()