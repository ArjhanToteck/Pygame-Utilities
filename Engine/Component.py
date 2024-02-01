import Engine

# this is the barebones template required for components. more often than not, sprites will be of better use unless you want to make something like a background.
class Component:
	def __init__(self, parent = None):
		
		# track component in GameManager
		Engine.GameManager.components.append(self)

		# create children list
		self.children = []

		if parent != None:
			parent.addChild(self)

	
	def addChild(self, child):
		self.children.append(child)
		child.parent = self


	def removeChild(self, child):
		self.children.remove(child)
		child.parent = None


	def onUpdate(self):
		pass


	def destroy(self):		
		# destroy colliders
		if(self.colliders != None):
			for collider in self.colliders:
				collider.destroy()

		# remove self from global record
		Engine.GameManager.components.remove(self)

		# remove self from parent
		self.parent.removeChild(self)
