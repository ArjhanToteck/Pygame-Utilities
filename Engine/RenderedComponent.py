import Engine

# this is the barebones template required for components. more often than not, sprites will be of better use unless you want to make something like a background.
class RenderedComponent(Engine.Component):
	def __init__(self, visible = True, layer = 1, parent = None):
		super().__init__(parent)

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