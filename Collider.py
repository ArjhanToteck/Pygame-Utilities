import pygame

from GameManager import GameManager
from Vector2 import Vector2
from enum import Enum

# this is a default collider class not meant for actual use outside of being inherited by the real types of colliders
class Collider:
	def __init__(self, parent, pivot = None, offset = None, position = None, enabled = True, isTrigger = False, followParent = True, visible = False):
		# parent gameObject
		self.parent = parent
		self.enabled = enabled
		self.isTrigger = isTrigger
		self.followParent = followParent

		self.currentCollisions = []

		self.visible = visible

		# TODO: improve pivot system to also factor in the parent sprite object pivot
		# default pivot
		if pivot == None:
			self.pivot = parent.pivot.clone()
		else:
			self.pivot = pivot

		# default offset
		if offset == None:
			self.offset = Vector2(0, 0)
		else:
			self.offset = offset

		# default position
		if position == None:
			self.position = parent.position.clone()
		else:
			self.position = position
			
		# add self to global collider list
		GameManager.colliders.append(self)

		# add self to parent collider list
		parent.colliders.append(self)


	def destroy(self):
		# remove self from global collider list
		GameManager.colliders.remove(self)

		# remove self from parent
		self.parent.colliders.remove(self)


	def updateCollisions(self):
		pass


	def requestMovement(self):
		pass


	def onRender(self):
		pass


	def onCollisionEnter(self, collision):
		pass


	def onCollisionExit(self, collision):
		pass


	def onCollisionStay(self, collision):
		pass


	def onTriggerEnter(self, collision):
		pass


	def onTriggerExit(self, collision):
		pass


	def onTriggerStay(self, collision):
		pass


class Collision:

	def __init__(self, selfCollider, otherCollider, collisionType, collisionPoint, overlap, justEntered = True):
		self.collisionType = collisionType
		self.selfCollider = selfCollider
		self.otherCollider = otherCollider
		self.collisionPoint = collisionPoint
		self.overlap = overlap
		self.justEntered = justEntered

	# enum for collision types
	class CollisionType(Enum):
		Trigger = 0
		Collision = 1


class RectangleCollider(Collider):
	def __init__(self, parent, pivot = None, offset = None, position = None, size = None, enabled = True, isTrigger = False, followParent = True, visible = False):
		
		# set default size
		if size == None:
			# by default, match parent size
			self.size = Vector2(parent.size.x, parent.size.y)
		else:
			self.size = size

		# call base init
		super().__init__(parent, pivot, offset, position, enabled, isTrigger, followParent, visible)


	def updateCollisions(self, callEvents = True):
		collisions = []

		# loop through colliders in scene
		for otherCollider in GameManager.colliders:

			# skip own collider
			if otherCollider == self:
				continue

			collision = None

			# check if other rectangle collider
			if isinstance(otherCollider, RectangleCollider):
				# calculate pivot offsets
				selfPivotOffset = (self.size / 2) * self.pivot
				otherPivotOffset = (otherCollider.size / 2) * otherCollider.pivot

				# calculate adjusted positions of rectangles
				selfLeft = self.position.x - selfPivotOffset.x + self.offset.x - (self.size.x / 2)
				selfRight = self.position.x - selfPivotOffset.x + self.offset.x + (self.size.x / 2)
				selfBottom = self.position.y - selfPivotOffset.y + self.offset.y - (self.size.y / 2)
				selfTop = self.position.y - selfPivotOffset.y + self.offset.y + (self.size.y / 2)
				
				otherLeft = otherCollider.position.x - otherPivotOffset.x + otherCollider.offset.x - (otherCollider.size.x / 2)
				otherRight = otherCollider.position.x - otherPivotOffset.x + otherCollider.offset.x + (otherCollider.size.x / 2)
				otherBottom = otherCollider.position.y - otherPivotOffset.y + otherCollider.offset.y - (otherCollider.size.y / 2)
				otherTop = otherCollider.position.y - otherPivotOffset.y + otherCollider.offset.y + (otherCollider.size.y / 2)

				# check for overlap on both axes
				overlap = Vector2()

				overlap.x = max(0, min(selfRight, otherRight) - max(selfLeft, otherLeft))
				overlap.y = max(0, min(selfTop, otherTop) - max(selfBottom, otherBottom))
				
				# collision occurred
				if overlap.x > 0 and overlap.y > 0:
					# get collision point
					collisionPoint = Vector2(max(selfLeft, otherLeft), max(selfTop, otherTop))

					# get collision data
					
					if selfLeft > otherLeft:
						overlap.x = -overlap.x
				
					if selfBottom > otherBottom:
						overlap.y = -overlap.y

					collision = Collision(self, otherCollider, Collision.CollisionType.Collision, collisionPoint, overlap)

			else:
				# TODO: implement collisions with other types
				pass

			# check if a collision of any type was detected
			if collision != None:
				collisions.append(collision)

				# mark collision as trigger event if applicable
				if self.isTrigger or otherCollider.isTrigger:
					collision.collisionType = Collision.CollisionType.Trigger

				# check if collision is already accounted for
				for otherCollision in self.currentCollisions:
					# check if the current collision already has the other collider
					if otherCollision.otherCollider == otherCollider:
						# make sure the collision knows it isn't new (onCollisionStay instead of onCollisionEnter)
						collision.justEntered = False
						break

				# check if we need to call events
				if callEvents:
					if collision.collisionType == Collision.CollisionType.Trigger:
						# trigger and justEntered
						if collision.justEntered:
							self.onTriggerEnter(collision)
							
						# trigger and staying
						else:
							self.onTriggerStay(collision)
					else:						
						# collider and justEntered
						if collision.justEntered:
							self.onCollisionEnter(collision)

						# collider and staying
						else:
							self.onCollisionStay(collision)

		# overwrite old collision array, but only if callEvents to not interfere with the game loop
		if callEvents:
			self.currentCollisions = collisions

		# return collision array
		return collisions


	def requestMovement(self, originalPosition, targetPosition):
		# this is a fake test collision, so we shouldn't call events and interfere with the game loop
		currentCollisions = self.updateCollisions(callEvents = False)
		
		permittedPosition = targetPosition

		for collision in currentCollisions:
			# make sure it's not a trigger
			if collision.collisionType == Collision.CollisionType.Collision:

				if isinstance(collision.otherCollider, RectangleCollider):
					overlap = collision.overlap

					if abs(collision.overlap.x) < abs(collision.overlap.y):
						overlap.y = 0
					elif abs(collision.overlap.x) > abs(collision.overlap.y):
						overlap.x = 0

					currentPermittedPosition = permittedPosition - overlap

					# set permittedPosition to currentPermitedPosition
					if Vector2.distance(currentPermittedPosition, originalPosition) < Vector2.distance(permittedPosition, originalPosition):
						permittedPosition = currentPermittedPosition

		return permittedPosition

	
	def onRender(self):
		if self.visible:
			color = (255, 0, 230)

			# get screen position of sprite (top left corner)
			screenPosition = GameManager.worldToScreenPosition(self.position + self.offset)

			# center of sprite (default pivot)
			pivotOffset = (self.size / 2) * GameManager.worldUnitSize

			# invert y of pivot
			pivotYInverted = self.pivot.clone()
			pivotYInverted.y *= -1

			# add pivot to offset (percentage of size)
			pivotOffset += pivotYInverted * (self.size / 2) * GameManager.worldUnitSize

			# subtract pivot
			screenPosition -= pivotOffset

			pygame.draw.rect(GameManager.screen, color, pygame.Rect(screenPosition.x, screenPosition.y, self.size.x * GameManager.worldUnitSize.x, self.size.y * GameManager.worldUnitSize.y),  2)


class CircleCollider(Collider):
	pass


class ImageCollider(Collider):
	pass