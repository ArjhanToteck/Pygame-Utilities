from ssl import VERIFY_ALLOW_PROXY_CERTS
from GameManager import GameManager
from GameObject import GameObject
from Sprite import Sprite
from Vector2 import Vector2
from Player import Player

import Collider

import pygame

# this class contains all the game objects and stuff for the scene
class StoreView:

	# this is called when the scene is opened. creates all the gameObjects it needs.
	@staticmethod
	def start():
		# store
		background = Sprite(imagePath = "Images/FloorAndWalls.png", size = GameManager.screenSizeWorldUnits, layer = 0)

		salesTable = Sprite(imagePath = "Images/SalesTable.png", position = Vector2(0, 4), layer = 2)
		clock = Sprite(imagePath = "Images/Clock.png", position = Vector2(5, 4), layer = 2)
		lamp = Sprite(imagePath = "Images/Lamp.png", position = Vector2(-5, 4), layer = 2)

		rug = Sprite(imagePath = "Images/Rug.png", position = Vector2(0, -1), layer = 0)

		couches = Sprite(imagePath = "Images/Couches.png", position = Vector2(-12, 3), pivot = Vector2(-1, 1), layer = 2)
		tablesAndChairs = Sprite(imagePath = "Images/TablesAndChairs.png", position = Vector2(12, 3), pivot = Vector2(1, 1), layer = 2)

		# create player
		player = Player(imagePath = "Images/Player.png", size = Vector2(3, 3))