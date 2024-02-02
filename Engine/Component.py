import Engine

# this is the barebones template required for components, more of a loose abstract class than something actual useful
# TODO: add rotation and reflection, make affecting parent affect child
class Component():
	def __init__(self, parent = None, position = None, size = None, pivot = None):
		
		# track component in GameManager
		Engine.GameManager.components.append(self)

		# default position (world units)
		if position == None:
			if parent == None:
				self.position = Engine.Vector2(0, 0)
			else:
				self.position = parent.position.clone()
		else:
			self.position = position

		# set default for pivot (relative coordinates: (0, 0) is center, (1, 1) is top right, so on)
		if pivot == None:
			# (0, 0) is center
			self.pivot = Engine.Vector2(0, 0)
		else:
			self.pivot = pivot

		# set default for size (world units)
		if size == None:
			self.size = Engine.Vector2(1, 1) 
		else:
			self.size = size

		# create children list
		self.children = []

		# add self to parent's children if applicable
		if parent != None:
			parent.addChild(self)

	
	def addChild(self, child):
		self.children.append(child)
		child.parent = self


	def removeChild(self, child):
		self.children.remove(child)
		child.parent = None


	def destroy(self):		
		# destroy colliders
		if(self.colliders != None):
			for collider in self.colliders:
				collider.destroy()

		# remove self from global record
		Engine.GameManager.components.remove(self)

		# remove self from parent
		self.parent.removeChild(self)

	
	def instantiate(self, parent = None, position = None):
		clonePosition = position

		# copy original position by default
		if clonePosition == None:
			clonePosition = self.position

		positionChange = clonePosition - self.position

		clone = Component(parent, clonePosition, self.size, self.pivot)

		# make sure to clone children too
		for child in self.children:
			child.instantiate(clone, child.position + positionChange)

		return clone


	def setSize(self, size):
		self.size = size

		# TODO: scale children as well


	def setSizePixels(self, size):
		self.setSize(size / Engine.GameManager.worldUnitSize)


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
			if Engine.Vector2.distance(currentPermittedPosition, originalPosition) < Engine.Vector2.distance(permittedPosition, originalPosition):
				permittedPosition = currentPermittedPosition

		# move to the permitted position
		self.position = permittedPosition

		# TODO: make this less collider reliant, maybe move this logic to the collider objects
		for collider in self.colliders:
				collider.position = self.position
		
		return permittedPosition
	
		# TODO: make this less collision dependent, fix all the collision stuff 

		"""# move children along with parent
		for child in self.children:
			child.move(movement)"""
	

	def moveTowards(self, targetPosition, movementStep):
		# TODO: implement this
		pass


	def setPosition(self, position):
		self.position = position


	def setPositionInPixels(self, position):
		self.setPosition(position / Engine.GameManager.worldUnitSize)


	def getPivotOffset(self, centerFirst = True):
		pivotOffset = Engine.Vector2(0, 0)

		if (centerFirst):
			# center (default pivot)
			pivotOffset = -(self.size / 2)

			# reflect y axis
			pivotOffset.y *= -1
		
		# apply the actual pivot (not just 0,0)
		pivotOffset += (self.size / 2) * -self.pivot		

		return pivotOffset
	
	

	def onUpdate(self):
		pass