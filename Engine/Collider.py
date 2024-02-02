import importlib

import Engine

from enum import Enum

# this is a default collider class not meant for actual use outside of being inherited by the real types of colliders
# TODO: incorporate Component class into this
class Collider(Engine.RenderedComponent):

	debugColor = (255, 0, 230)

	def __init__(self, offset = None, enabled = True, isTrigger = False, enableCollisionEvents = True, visible = False, layer = 999, parent = None, position = None, size = None, pivot = None):

		super().__init__(visible, layer, parent, position, size, pivot)

		# parent component
		self.enabled = enabled
		self.isTrigger = isTrigger
		self.enableCollisionEvents = enableCollisionEvents

		self.currentCollisions = []

		# TODO: improve pivot system to also factor in the parent sprite object pivot
		# default pivot
		if pivot == None:
			self.pivot = Engine.Vector2(0, 0)
		else:
			self.pivot = pivot

		# default offset
		if offset == None:
			self.offset = Engine.Vector2(0, 0)
		else:
			self.offset = offset

		# default position
		if position == None:
			self.position = parent.position.clone()
		else:
			self.position = position
			
		# add self to global collider list
		Engine.GameManager.colliders.append(self)

		# add self to parent collider list
		self.parent.colliders.append(self)


	def instantiate(self, parent = None, position = None):
		clonePosition = position

		# copy original position by default
		if clonePosition == None:
			clonePosition = self.position

		positionChange = clonePosition - self.position

		clone = Collider(self.offset, self.enabled, self.isTrigger, self.enableCollisionEvents, self.visible, self.layer, parent, position, self.size, self.pivot)

		# make sure to clone children too
		for child in self.children:
			child.instantiate(clone, child.position + positionChange)

		return clone


	def destroy(self):
		# remove self from global collider list
		Engine.GameManager.colliders.remove(self)

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
	def __init__(self, offset = None, enabled = True, isTrigger = False, enableCollisionEvents = True, visible = False, layer = 999, parent = None, position = None, size = None, pivot = None):
		
		# call base init
		super().__init__(offset, enabled, isTrigger, enableCollisionEvents, visible, layer, parent, position, size, pivot)

		# set default size
		if size == None:
			# by default, match parent size
			self.size = Engine.Vector2(parent.size.x, parent.size.y)
		else:
			self.size = size


	def instantiate(self, parent = None, position = None):
		clonePosition = position

		# copy original position by default
		if clonePosition == None:
			clonePosition = self.position

		positionChange = clonePosition - self.position

		clone = RectangleCollider(self.offset, self.enabled, self.isTrigger, self.enableCollisionEvents, self.visible, self.layer, parent, position, self.size, self.pivot)

		# make sure to clone children too
		for child in self.children:
			child.instantiate(clone, child.position + positionChange)

		return clone


	def updateCollisions(self, callEvents = True):
		# dont need to check every frame if enable collision events is false
		if callEvents and not self.enableCollisionEvents:
			return

		collisions = []

		# loop through colliders in scene
		for otherCollider in Engine.GameManager.colliders:

			# skip own collider
			if otherCollider == self:
				continue

			collision = None

			# check if other rectangle collider
			if isinstance(otherCollider, RectangleCollider):

				# calculate pivot offsets
				selfCalculatedPosition = self.position + self.offset + self.getPivotOffset(False) + self.parent.getPivotOffset(False)
				otherCalculatedPosition = otherCollider.position + otherCollider.offset + otherCollider.getPivotOffset(False) + otherCollider.parent.getPivotOffset(False)

				# calculate adjusted positions of rectangles
				selfLeft = selfCalculatedPosition.x - (self.size.x / 2)
				selfRight = selfCalculatedPosition.x + (self.size.x / 2)
				selfBottom = selfCalculatedPosition.y - (self.size.y / 2)
				selfTop = selfCalculatedPosition.y + (self.size.y / 2)
				
				otherLeft = otherCalculatedPosition.x - (otherCollider.size.x / 2)
				otherRight = otherCalculatedPosition.x + (otherCollider.size.x / 2)
				otherBottom = otherCalculatedPosition.y - (otherCollider.size.y / 2)
				otherTop = otherCalculatedPosition.y + (otherCollider.size.y / 2)

				# check for overlap on both axes
				overlap = Engine.Vector2()

				overlap.x = max(0, min(selfRight, otherRight) - max(selfLeft, otherLeft))
				overlap.y = max(0, min(selfTop, otherTop) - max(selfBottom, otherBottom))
				
				# collision occurred
				if overlap.x > 0 and overlap.y > 0:
					# get collision point
					collisionPoint = Engine.Vector2(max(selfLeft, otherLeft), max(selfTop, otherTop))

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
		# TODO: this kind of sucks. should probably fix.
		
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
					if Engine.Vector2.distance(currentPermittedPosition, originalPosition) < Engine.Vector2.distance(permittedPosition, originalPosition):
						permittedPosition = currentPermittedPosition

		return permittedPosition


	def onRender(self):
		if self.visible:
			# get screen position of collider with pivot and pivot offset factored in
			screenPosition = Engine.GameManager.worldToScreenPosition(self.position + self.offset + self.getPivotOffset() + self.parent.getPivotOffset(False))

			Engine.pygame.draw.rect(Engine.GameManager.screen, Collider.debugColor, Engine.pygame.Rect(screenPosition.x, screenPosition.y, self.size.x * Engine.GameManager.worldUnitSize.x, self.size.y * Engine.GameManager.worldUnitSize.y), 2)


class CircleCollider(Collider):
	pass


class ImageCollider(Collider):
	pass


Collider.Collision = Collision
Collider.RectangleCollider = RectangleCollider
Collider.CircleCollider = CircleCollider
Collider.ImageCollider = ImageCollider


importlib.reload(Engine)