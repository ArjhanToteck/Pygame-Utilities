import pygame
import warnings
import sys
import threading

from Vector2 import Vector2

class GameManager:
	# pygame settings
	running = True
	screen = None
	clock = None
	gameLoopThread = None
	deltaTime = 0
	worldUnitSize = Vector2(50, 50) # number of pixels per world unit
	screenSizePixels = Vector2(1280, 720)
	screenSizeWorldUnits = screenSizePixels / worldUnitSize

	gameObjects = []
	colliders = []

	# stores pygame events on a given frame
	pygameEvents = []
	keysDown = []

	# stores functions to render stuff here, the key being the render layer
	renderQueue = {}
	
	@staticmethod
	def quit():
		GameManager.running = False
		pygame.quit()
		sys.exit()

	@staticmethod
	def nextFrame():
		while GameManager.running == True:
			# clear events for this frame
			GameManager.pygameEvents = []
			
			# event queue
			for event in pygame.event.get():
				# on window closing
				if event.type == pygame.QUIT:
					GameManager.running = False
					GameManager.quit()

				# adds event to list for current frame
				GameManager.pygameEvents.append(event)
					
			# get key presses
			GameManager.keysDown = pygame.key.get_pressed()

			"""# detect collisions
			for collider in GameManager.colliders:
				collider.checkCollisions()"""

			# call update events on gameObjects
			for gameObject in GameManager.gameObjects:
				gameObject.onUpdate()

			# loop through render layers
			for layer in GameManager.renderQueue:
				# render everything in the current layer
				for event in GameManager.renderQueue[layer]:
					event()            

			# flip display for screen
			pygame.display.flip()
			
			# next frame
			GameManager.deltaTime = GameManager.clock.tick() / 1000

	@staticmethod
	def setUpGame(callback = None):
		# pygame setup
		pygame.init()
		GameManager.screen = pygame.display.set_mode(GameManager.screenSizePixels.toArray())
		GameManager.clock = pygame.time.Clock()
		GameManager.running = True

		if(callback != None):
			callbackThread = threading.Thread(target = callback)
			callbackThread.start()

	@staticmethod
	def addToRenderQueue(renderer, layer):
		# checks if layer already exists
		if(layer in GameManager.renderQueue):
			# add render function to queue
			GameManager.renderQueue[layer].append(renderer)
		else:
			# create new render layer with the renderer
			GameManager.renderQueue[layer] = [renderer]

		# make sure to sort it after changing
		GameManager.renderQueue = dict(sorted(GameManager.renderQueue.items()))

	@staticmethod
	def removeFromRenderQueue(renderer, layer):

		# checks if the renderqueue doesn't exist
		if not GameManager.renderQueue[layer]:
			warnings.warn("The layer of the renderer you are trying to remove is not in the queue.")
		
		# checks if renderer is not in the queue/layer
		elif  renderer not in GameManager.renderQueue[layer]:
			warnings.warn("The renderer you are trying to remove is not in the queue or is not in the specified layer.")

		else:
			GameManager.renderQueue[layer].remove(renderer)