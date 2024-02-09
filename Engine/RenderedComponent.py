import warnings

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
		self.hiddenByParent = False

		# check if we have a parent and the parent is hidden, but self is not hidden
		if hasattr(self, "parent") and self.parent != None and isinstance(self.parent, RenderedComponent) and not self.parent.visible:
			self.hiddenByParent = True
			self.visible = False

		# show component if visible (in renderQueue, of course)
		if self.visible:
			self.show()

		# track component in GameManager
		Engine.GameManager.components.append(self)


	def show(self, overrideParentVisibility = False):
		if self.hiddenByParent and not overrideParentVisibility:			
			warnings.warn("Attempting to show an object hidden by parent.")
			return
		elif self.hiddenByParent and overrideParentVisibility:
			self.hiddenByParent = False

		self.visible = True
		Engine.GameManager.addToRenderQueue(self.onRender, self.layer)
		
		for child in self.children:
			if child.hiddenByParent == True:
				child.hiddenByParent = False
				child.show()


	
	def hide(self, hiddenByParent = False):
		self.visible = False
		Engine.GameManager.removeFromRenderQueue(self.onRender, self.layer)
		
		self.hiddenByParent = hiddenByParent
		
		for child in self.children:
			if child.visible == True:
				child.hiddenByParent = True
				child.hide(True)

		
	def onRender(self):
		pass


	def onCollision(self, localCollider, otherCollider):
		pass

	
	def onTrigger(self, localCollider, otherCollider):
		pass


	def destroy(self):
		self.hide()

		super().destroy()


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