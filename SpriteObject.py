from shutil import move
import pygame

from GameManager import GameManager
from Vector2 import Vector2
from Vector2Bool import Vector2Bool
from GameObject import GameObject

# sprites are a template for GameObjects that rely on a 2d image
class SpriteObject(GameObject):
	def __init__(self, position = None, size = None, visible = True, layer = 1, reflection = None, pivot = None, spritePath = None, sprite = None):

		# set sprite
		if sprite != None:
			self.updateSprite(sprite)

		# set sprite with path
		if spritePath != None:
			self.updateSpriteByPath(spritePath)
			
		# set default for position (world units)
		if position == None:
			self.position = Vector2(0, 0)
		else:
			self.position = position

		# sprite transformations

		# set default for reflection
		if reflection == None:
			self.setReflection(Vector2Bool(False, False))
		else:
			self.setReflection(reflection)
		
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

		# update sprite transofmrations
		self.updateSpriteTransformations()

		# set default for pivot (distance from center in percentage of total size)
		if pivot == None:
			self.pivot = Vector2(0, 0)
		else:
			self.pivot = pivot
		
		# do the regular __init__ for gameObjects
		super().__init__(visible, layer)


	def updateSpriteTransformations(self):		
		# account for size (might not be set yet)
		if hasattr(self, "size"):
			self.transformedSprite = pygame.transform.scale(self.transformedSprite, (self.size * GameManager.worldUnitSize).toArray())

		# account for reflection (might not be set yet)
		if hasattr(self, "reflection"):
			self.transformedSprite = pygame.transform.flip(self.transformedSprite, self.reflection.x, self.reflection.y)


	def updateSprite(self, sprite):
		self.sprite = sprite

		# copy sprite into transformedSprite
		# transformedSprite will have all the transformations applied to it and will be the actual drawn image
		self.transformedSprite = self.sprite.copy()

		self.updateSpriteTransformations()


	def updateSpriteByPath(self, spritePath):
		self.updateSprite(pygame.image.load(spritePath))


	def setReflection(self, reflection):
		self.reflection = reflection
		self.updateSpriteTransformations()


	def setSize(self, size):
		self.size = size
		self.updateSpriteTransformations()


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
		
		return permittedPosition


	def setPosition(self, position):
		self.position = position


	def setPositionInPixels(self, position):
		self.setPosition(position / GameManager.worldUnitSize)


	def getPivotOffset(self, centerFirst = True):
		pivotOffset = Vector2(0, 0)

		if (centerFirst):
			# center sprite (default pivot)
			pivotOffset = -(self.size / 2)

			# reflect y axis
			pivotOffset.y *= -1
		
		# apply the actual pivot (not just 0,0)
		pivotOffset += (self.size / 2) * -self.pivot		

		return pivotOffset

	# by default, game objects will render self.sprite in self.position with self.size
	def onRender(self):
		if self.visible:

			# get screen position of sprite with pivot offset factored in
			screenPosition = GameManager.worldToScreenPosition(self.position + self.getPivotOffset())

			# draw sprite at position
			GameManager.screen.blit(self.transformedSprite, screenPosition.toArray())

		# perform normal gameObject render
		super().onRender()