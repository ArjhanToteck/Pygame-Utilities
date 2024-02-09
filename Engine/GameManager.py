import importlib
import warnings
import sys

import Engine

# TODO: fps sucks now bc i rushed some stuff. look into optimizing stuff

class GameManager:
	# settings	
	worldUnitSize = Engine.Vector2(50, 50) # number of pixels per world unit
	screenSizePixels = Engine.Vector2(1280, 720)

	running = True
	screen = None
	clock = None
	gameLoopThread = None
	deltaTime = 0
	screenSizeWorldUnits = screenSizePixels / worldUnitSize

	components = []
	colliders = []

	# stores pygame events on a given frame
	pygameEvents = []
	keysDown = {}
	keysPressed = {}
	mousePressed = False
	mousePosition = Engine.Vector2(0, 0)
	mouseRaycasts = []

	# stores functions to render stuff here, the key being the render layer
	renderQueue = {}
  
	@classmethod
	def updateScreenSizePixels(cls, size):
		cls.screen = Engine.pygame.display.set_mode(size.toArray(), Engine.pygame.RESIZABLE)
		cls.screenSizePixels = size.clone()
		cls.screenSizeWorldUnits = size / cls.worldUnitSize
  
 
	@classmethod
	def updateScreenSizeWorldUnits(cls, size):
		cls.updateScreenSizePixels(size * cls.worldUnitSize)
  
	
	@classmethod
	def quit(cls):
		cls.running = False
		Engine.pygame.quit()
		sys.exit()


	@classmethod
	def nextFrame(cls):
		while cls.running == True:
			# clear events for this frame
			cls.pygameEvents = []
			cls.keysPressed = {}
			cls.mousePressed = False
			
			# event queue
			for event in Engine.pygame.event.get():
				# on window closing
				if event.type == Engine.pygame.QUIT:
					cls.running = False
					cls.quit()


				# resize window
				if event.type == Engine.pygame.VIDEORESIZE:
					cls.updateScreenSizePixels(Engine.Vector2(event.w, event.h))


				# key press
				if event.type == Engine.pygame.KEYUP:
					cls.keysPressed[event.key] = True

				# mouse press
				if event.type == Engine.pygame.MOUSEBUTTONUP:
					cls.mousePressed = True

				# adds event to list for current frame
				cls.pygameEvents.append(event)
					
			# get key presses
			# TODO: better input system with its own class probably
			cls.keysDown = Engine.pygame.key.get_pressed()

			# get mouse position
			mousePosition = Engine.pygame.mouse.get_pos()
			mousePosition = Engine.Vector2(mousePosition[0], mousePosition[1])
			cls.mousePosition = cls.screenToWorldPosition(mousePosition)
			
			cls.mouseRaycasts = Engine.Collider.raycast(cls.mousePosition)

			# update collisions
			for collider in GameManager.colliders:
				collider.updateCollisions()

			# call update events on components
			for component in cls.components:
				component.onUpdate()

			# loop through render layers
			for layer in cls.renderQueue:
				# render everything in the current layer
				for event in cls.renderQueue[layer]:
					event()			

			# flip display for screen
			Engine.pygame.display.flip()
			
			# next frame
			cls.deltaTime = cls.clock.tick() / 1000

			# print fps
			#print(1 / cls.deltaTime)
			

	@classmethod
	def setUpGame(cls, worldUnitSize = None, screenSizePixels = None):
		# pygame setup
		Engine.pygame.init()
		cls.updateScreenSizePixels(screenSizePixels)
		cls.clock = Engine.pygame.time.Clock()
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
	def showAllColliders(cls):
		for component in cls.components:
			if isinstance(component, Engine.Collider):
				component.show()
		

	@classmethod
	def hideAllColliders(cls):
		for component in cls.components:
			# TODO: figure out wtf is happening with Collider
			if isinstance(component, Engine.Collider):
				component.hide()
	

	@classmethod
	def worldToScreenPosition(cls, worldPosition):
		# invert y axis
		worldPositionYInverted = Engine.Vector2(worldPosition.x, -worldPosition.y)
		
		# scale world units by size in pixels
		screenPosition = worldPositionYInverted * cls.worldUnitSize

		# add offset to account for center of screen		
		centerOffsetPixels = Engine.Vector2(cls.screenSizePixels.x / 2, cls.screenSizePixels.y / 2)
		screenPosition += centerOffsetPixels

		return screenPosition
	

	@classmethod
	def screenToWorldPosition(cls, screenPosition):
				
		# divide world units by size in pixels
		worldPosition = screenPosition / cls.worldUnitSize
		
		# add offset to account for center of screen
		centerOffsetWorldUnits = Engine.Vector2(cls.screenSizeWorldUnits.x / 2, cls.screenSizeWorldUnits.y / 2)
		worldPosition -= centerOffsetWorldUnits

		worldPosition.y *= -1

		return worldPosition

importlib.reload(Engine)