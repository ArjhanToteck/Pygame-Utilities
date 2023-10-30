import pygame

from GameManager import GameManager
from Vector2 import Vector2

class GameObject:
	def __init__(self, visible = True, layer = 1):
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


	# by default, game objects will render self.image in self.position with self.size
	def onRender(self):
		pass

	def onUpdate(self):
		pass

	def destroy(self):
		GameManager.gameObjects.remove(self)
		GameManager.onUpdate.remove(self.onUpdate)
		self.hide()