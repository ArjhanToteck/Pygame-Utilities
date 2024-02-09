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

		self.hasMouse = False

	def onUpdate(self):
		# check if mouse raycast hit collider
		if self.collider in Engine.GameManager.mouseRaycasts:
			# check if click
			if Engine.GameManager.mousePressed:
				# click
				self.onClick()
			else:

				# check if we already had the mouse before
				if self.hasMouse:
					# mouse is remaining on button
					self.onMouseHover()
				else:
					# mouse is just entering button this frame
					self.onMouseEnter()

			# mark as having the mouse
			self.hasMouse = True

		# check if we had the mouse last frame
		elif self.hasMouse:
			# mark as no longer having the mouse
			self.hasMouse = False

			# the mouse just exited the button
			self.onMouseExit()


	def onMouseEnter(self):
		pass	


	def onMouseHover(self):
		pass
	

	def onMouseExit(self):
		pass
	

	def onMouseClick(self):
		pass


	def onClick(self):
		pass