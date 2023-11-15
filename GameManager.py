import pygame
import warnings
import sys

from Vector2 import Vector2

class GameManager:
	# settings	
	worldUnitSize = Vector2(50, 50) # number of pixels per world unit
	screenSizePixels = Vector2(1280, 720)

	running = True
	screen = None
	clock = None
	gameLoopThread = None
	deltaTime = 0
	screenSizeWorldUnits = screenSizePixels / worldUnitSize

	gameObjects = []
	colliders = []

	# stores pygame events on a given frame
	pygameEvents = []
	keysDown = []

	# stores functions to render stuff here, the key being the render layer
	renderQueue = {}
	
	@classmethod
	def quit(cls):
		cls.running = False
		pygame.quit()
		sys.exit()

	@classmethod
	def nextFrame(cls):
		while cls.running == True:
			# clear events for this frame
			cls.pygameEvents = []
			
			# event queue
			for event in pygame.event.get():
				# on window closing
				if event.type == pygame.QUIT:
					cls.running = False
					cls.quit()

				# adds event to list for current frame
				cls.pygameEvents.append(event)
					
			# get key presses
			cls.keysDown = pygame.key.get_pressed()

			# update collisions
			for collider in GameManager.colliders:
				collider.updateCollisions()

			# call update events on gameObjects
			for gameObject in cls.gameObjects:
				gameObject.onUpdate()

			# loop through render layers
			for layer in cls.renderQueue:
				# render everything in the current layer
				for event in cls.renderQueue[layer]:
					event()            

			# flip display for screen
			pygame.display.flip()
			
			# next frame
			cls.deltaTime = cls.clock.tick() / 1000

	@classmethod
	def setUpGame(cls, worldUnitSize = None, screenSizePixels = None):
		# pygame setup
		pygame.init()
		cls.screen = pygame.display.set_mode(cls.screenSizePixels.toArray())
		cls.clock = pygame.time.Clock()
		cls.running = True

		if worldUnitSize != None:
			cls.worldUnitSize = worldUnitSize

		
		if screenSizePixels != None:
			cls.screenSizePixels = screenSizePixels

	@classmethod
	def addToRenderQueue(cls, renderer, layer):
		# checks if layer already exists
		if(layer in cls.renderQueue):
			# add render function to queue
			cls.renderQueue[layer].append(renderer)
		else:
			# create new render layer with the renderer
			cls.renderQueue[layer] = [renderer]

		# make sure to sort it after changing
		cls.renderQueue = dict(sorted(cls.renderQueue.items()))

	@classmethod
	def removeFromRenderQueue(cls, renderer, layer):

		# checks if the renderqueue doesn't exist
		if not cls.renderQueue[layer]:
			warnings.warn("The layer of the renderer you are trying to remove is not in the queue.")
		
		# checks if renderer is not in the queue/layer
		elif  renderer not in cls.renderQueue[layer]:
			warnings.warn("The renderer you are trying to remove is not in the queue or is not in the specified layer.")

		else:
			cls.renderQueue[layer].remove(renderer)

	
	@classmethod
	def worldToScreenPosition(cls, worldPosition):
		# invert y axis
		worldPositionYInverted = Vector2(worldPosition.x, -worldPosition.y)

		pixelCenter = Vector2(cls.screenSizePixels.x / 2, cls.screenSizePixels.y / 2)

		# scale world units by size in pixels
		pixelPosition = worldPositionYInverted * cls.worldUnitSize

		# add offset to account for center of screen
		pixelPosition += pixelCenter

		return pixelPosition
