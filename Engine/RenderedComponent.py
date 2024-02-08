import Engine

from Layers import Layers

# this class automatically handles the events for rendering something in GameManager's queue. For actually displaying images, SpriteObject is usually recommendable, though this can be useful for custom render functions.
class RenderedComponent(Engine.Component):
    
	def __init__(self, visible = True, layer = Layers.default, parent = None, position = None, size = None, pivot = None):
		super().__init__(parent, position, size, pivot)

		self.colliders = []

		self.layer = layer

		# while this can be set at instantiation, helper functions should be used to hide and show the object afterwards
		self.visible = visible

		# show component if visible (in renderQueue, of course)
		if self.visible:
			self.show()

		# track component in GameManager
		Engine.GameManager.components.append(self)


	def show(self):
		self.visible = True
		Engine.GameManager.addToRenderQueue(self.onRender, self.layer)

	
	def hide(self):
		self.visible = False
		Engine.GameManager.removeFromRenderQueue(self.onRender, self.layer)

		
	def onRender(self):
		pass


	def onCollision(self, localCollider, otherCollider):
		pass

	
	def onTrigger(self, localCollider, otherCollider):
		pass


	def destroy(self):
		# destroy colliders
		if(self.colliders != None):
			for collider in self.colliders:
				collider.destroy()

		# remove self from global record
		Engine.GameManager.components.remove(self)

		# make sure not to be rendered
		self.hide()

	def instantiate(self, parent = None, position = None):
		clonePosition = position

		# copy original position by default
		if clonePosition == None:
			clonePosition = self.position

		positionChange = clonePosition - self.position

		clone = RenderedComponent(self.visible, self.layer, parent, position, self.size, self.pivot)

		# make sure to clone children too
		for child in self.children:
			child.instantiate(clone, child.position + positionChange)

		return clone