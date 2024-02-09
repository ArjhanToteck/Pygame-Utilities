import Engine

from Layers import Layers

class Button(Engine.Component):

	def __init__(self, collider = None, enabled = True, parent = None, position = None, size = None, pivot = None):
		super().__init__(parent, position, size, pivot)

		self.enabled = enabled
		
		if collider == None and self.parent and isinstance(self.parent, Engine.Collider):
			self.collider = self.parent
		else:
			self.collider = collider

	def onUpdate(self):
		if self.collider in Engine.GameManager.mouseRaycasts:
			print("mouse hover")