from Engine import *

# this is the barebones template required for gameObjects. more often than not, sprites will be of better use unless you want to make something like a background.
class Component:
	def __init__(self, visible = True, layer = 1):
		self.colliders = []

		self.layer = layer

		# while this can be set at instantiation, helper functions should be used to hide and show the object afterwards
		self.visible = visible

		# show gameObject if visible (in renderQueue, of course)
		if self.visible:
			self.show()

		# track gameObject in GameManager
		GameManager.gameObjects.append(self)


	def show(self):
		self.visible = True
		GameManager.addToRenderQueue(self.onRender, self.layer)

	
	def hide(self):
		self.visible = False
		GameManager.removeFromRenderQueue(self.onRender, self.layer)


	# by default, game objects won't render anything except colliders for debug (use Sprite to render images)
	def onRender(self):
		# render colliders
		for collider in self.colliders:
			collider.onRender()


	def onUpdate(self):
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
		GameManager.gameObjects.remove(self)

		# make sure not to be rendered
		self.hide()
