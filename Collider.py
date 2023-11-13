from GameManager import GameManager
from Vector2 import Vector2
from enum import Enum

# TODO: implement actual collision, allow colliders to be added to GameObjects, create subclasses for different collider types

# this is a default collider class not meant for actual use outside of being inherited by the real types of colliders
class Collider:
	def __init__(self, parent, pivot = None, position = None, enabled = True, isTrigger = False, followParent = True, visible = False):
		# parent gameObject
		self.parent = parent
		self.enabled = enabled
		self.isTrigger = isTrigger
		self.followParent = followParent

		self.currentCollisions = []

		self.visible = visible # TODO: add a way to render colliders for debug (in non-default colliders)

		# default offset
		if pivot == None:
			pivot = Vector2(0, 0)

		# default position
		if position == None:
			position = parent.position
			
		# add self to global collider list
		GameManager.colliders.append(self)


	def destroy(self):
		# remove self from global collider list
		GameManager.colliders.remove(self)

		# remove self from parent
		self.parent.colliders.remove(self)
		
		# make sure not to be rendered
		self.hide()


	def updateCollisions(self):
		pass


	def onCollisionEnter(self):
		pass


	def onCollisionExit(self):
		pass


	def onCollisionStay(self):
		pass


	def onTriggerEnter(self):
		pass


	def onTriggerExit(self):
		pass


	def onTriggerStay(self):
		pass


	def onRender(self):
		pass


class Collision:

	def __init__(self, selfCollider, otherCollider, collisionType, collisionPoint, justEntered = True):
		self.collisionType = collisionType
		self.selfCollider = selfCollider
		self.otherCollider = otherCollider
		self.collisionPoint = collisionPoint
		self.justEntered = justEntered

	# enum for collision types
	class CollisionType(Enum):
		Trigger = 0
		Collision = 1


class RectangleCollider(Collider):
	def __init__(self, parent, offset=None, size = None, position=None, enabled=True, isTrigger=False, followParent=True, visible=False):
		
		# set default size
		if size == None:
			# by default, match parent size
			self.size = Vector2(parent.size.x, parent.size.y)
		else:
			self.size = size

		# call base init
		super().__init__(parent, offset, position, enabled, isTrigger, followParent, visible)


	def updateCollisions(self, callEvents = True):
		collisions = []

		# loop through colliders in scene
		for otherCollider in GameManager.colliders:

			collision = None

			# check if other rectangle collider
			if isinstance(otherCollider, RectangleCollider):
				# check for collision between two rectangles based on bounding boxes
				selfLeft = self.parent.position.x + self.offset.x
				selfRight = selfLeft + self.size.x
				selfTop = self.parent.position.y + self.offset.y
				selfBottom = selfTop + self.size.y

				otherLeft = otherCollider.parent.position.x + otherCollider.offset.x
				otherRight = otherLeft + otherCollider.size.x
				otherTop = otherCollider.parent.position.y + otherCollider.offset.y
				otherBottom = otherTop + otherCollider.size.y

				# check for overlap along both axes
				xOverlap = selfRight > otherLeft and selfLeft < otherRight
				yOverlap = selfBottom > otherTop and selfTop < otherBottom

				# collision occured
				if xOverlap and yOverlap:
					# get collision point
					collisionPoint = Vector2(max(selfLeft, otherLeft), max(selfTop, otherTop))

					# get collision data
					collision = Collision(self, otherCollider, Collision.CollisionType.Collision, collisionPoint)

			else:
				# TODO: implement collisions with other types
				pass

			# check if a collision of any type was detected
			if collision != None:
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
					if collision.isTrigger:
						# trigger and justEntered
						if collision.justEntered:
							self.onTriggerEnter()
							
						# trigger and staying
						else:
							self.onTriggerStay()
					else:						
						# collider and justEntered
						if collision.justEntered:
							self.onCollisionEnter()

						# collider and staying
						else:
							self.onCollisionStay()

		# overwrite old collision array
		self.currentCollisions = collisions

		# return collision array
		return self.currentCollisions
	
	def onRender(self):
		if self.visible:
			color = (255, 0, 230)

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

			GameManager.pygame.draw.rect(GameManager.screen, color, GameManager.pygame.Rect(screenPosition.x, screenPosition.y, self.size.x * GameManager.worldUnitSize, self.size.x * GameManager.worldUnitSize),  2)


class CircleCollider(Collider):
	pass


class ImageCollider(Collider):
	pass