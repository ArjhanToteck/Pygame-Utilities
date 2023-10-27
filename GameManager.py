import pygame
import threading
import warnings
import sys

from Vector2 import Vector2

class GameManager:
    # pygame settings
    running = True
    screen = None
    clock = None
    gameLoopThread = None
    deltaTime = 0
    worldUnitSize = Vector2(25, 25) # number of pixels per world unit

    # stores functions that will be called every frame
    updateEvents = []

    # stores functions to render stuff here, the key being the render layer
    renderQueue = {}
    
    @staticmethod
    def quit():
        GameManager.running = False
        pygame.quit()
        sys.exit()

    @staticmethod
    def gameLoop():
        while GameManager.running == True:
            # event queue
            for event in pygame.event.get():
                # on window closing
                if event.type == pygame.QUIT:
                    GameManager.running = False
                    GameManager.quit()
                    
            # call update event
            for event in GameManager.updateEvents:
                event()

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
    def setUpGame():
        # pygame setup
        pygame.init()
        GameManager.screen = pygame.display.set_mode((1280, 720))
        GameManager.clock = pygame.time.Clock()
        GameManager.running = True

        # start game loop
        gameLoopThread = threading.Thread(target = GameManager.gameLoop)
        gameLoopThread.start()

    @staticmethod
    def addToRenderQueue(renderer, layer):
        # checks if layer already exists
        if(layer in GameManager.renderQueue):
            # add render function to queue
            GameManager.renderQueue.append(renderer)
        else:
            # create new render layer with the renderer
            GameManager.renderQueue[layer] = [renderer]
            print("added to queue")

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