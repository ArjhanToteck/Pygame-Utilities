import Engine

# sprites are a template for components that rely on a 2d image
class SpriteObject(Engine.RenderedComponent):
	def __init__(self, reflection = None, spritePath = None, sprite = None, visible = True, layer = 1, parent = None, position = None, size = None, pivot = None):
		
		# do the regular __init__ for rendered components
		super().__init__(visible, layer, parent, position, size, pivot)

		# set sprite
		self.sprite = sprite
		if self.sprite != None:
			self.setSprite(self.sprite)

		# set sprite with path
		if spritePath != None:
			self.setSpriteByPath(spritePath)
			
		# set default for pivot (distance from center in percentage of total size)
		if pivot == None:
			self.pivot = Engine.Vector2(0, 0)
		else:
			self.pivot = pivot

		# sprite transformations

		# set default for reflection
		if reflection == None:
			self.setReflection(Engine.Vector2Bool(False, False))
		else:
			self.setReflection(reflection)
	
		# set default for size (world units)
		# while this can be set at instantiation, helper functions should be used to set the size of the object afterwards
		if size == None:
			# set size based on sprite
			if self.sprite != None:
				self.setSizePixels(Engine.Vector2(self.sprite.get_width(), self.sprite.get_height()))
			else:
				self.setSize(Engine.Vector2(1, 1))
		else:
			self.setSize(size)

		# update sprite transofmrations
		self.updateSpriteTransformations()

	
	def instantiate(self, parent = None, position = None):
		clonePosition = position

		# copy original position by default
		if clonePosition == None:
			clonePosition = self.position

		positionChange = clonePosition - self.position

		clone = SpriteObject(self.reflection, None, self.sprite, self.visible, self.layer, parent, position, self.size, self.pivot)

		# make sure to clone children too
		for child in self.children:
			child.instantiate(clone, child.position + positionChange)

		return clone


	def updateSpriteTransformations(self):
		if self.sprite == None:
			return

		# account for size (might not be set yet)
		if hasattr(self, "size"):
			self.transformedSprite = Engine.pygame.transform.scale(self.sprite, (self.size * Engine.GameManager.worldUnitSize).toArray())

		# account for reflection (might not be set yet)
		if hasattr(self, "reflection"):
			self.transformedSprite = Engine.pygame.transform.flip(self.transformedSprite, self.reflection.x, self.reflection.y)


	def setSprite(self, sprite):
		self.sprite = sprite

		# copy sprite into transformedSprite
		# transformedSprite will have all the transformations applied to it and will be the actual drawn image
		self.transformedSprite = self.sprite.copy()

		self.updateSpriteTransformations()


	def setSpriteByPath(self, spritePath):
		self.setSprite(Engine.pygame.image.load(spritePath))


	def setReflection(self, reflection):
		self.reflection = reflection
		self.updateSpriteTransformations()


	def setSize(self, size):
		super().setSize(size)
		self.updateSpriteTransformations()


	# by default, game objects will render self.sprite in self.position with self.size
	def onRender(self):
		if self.visible:

			# get screen position of sprite with pivot offset factored in
			screenPosition = Engine.GameManager.worldToScreenPosition(self.position + self.getPivotOffset())

			# draw sprite at position
			Engine.GameManager.screen.blit(self.transformedSprite, screenPosition.toArray())

		# perform normal component render
		super().onRender()