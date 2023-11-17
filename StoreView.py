from GameManager import GameManager
from GameObject import GameObject
from SpriteObject import SpriteObject
from Vector2 import Vector2
from Player import Player
from SpriteSheet import SpriteSheet

import Collider

# this class contains all the game objects and stuff for the scene
class StoreView:

	# this is called when the scene is opened. creates all the gameObjects it needs.
	@staticmethod
	def start():
		# create player
		playerSpriteSheet = SpriteSheet(imagePath = "Images/Player.png")
		playerSpriteSheet.sliceByRowsAndColumns(10, 6)
		player = Player(sprite = playerSpriteSheet.sprites[0][0], size = Vector2(3, 3))

		# store
		background = SpriteObject(spritePath = "Images/FloorAndWalls.png", size = GameManager.screenSizeWorldUnits, layer = 0)

		salesTable = SpriteObject(spritePath = "Images/SalesTable.png", position = Vector2(0, 4), layer = 2)
		Collider.RectangleCollider(parent = salesTable, isTrigger = False, pivot = Vector2(-1, 0), size = Vector2(0.25, salesTable.size.y), offset = Vector2(-salesTable.size.x / 2, 0))
		Collider.RectangleCollider(parent = salesTable, isTrigger = False, pivot = Vector2(0, 0), size = Vector2(0.5, salesTable.size.y))		
		Collider.RectangleCollider(parent = salesTable, isTrigger = False, pivot = Vector2(1, 0), size = Vector2(0.25, salesTable.size.y), offset = Vector2(salesTable.size.x / 2, 0))

		clock = SpriteObject(spritePath = "Images/Clock.png", position = Vector2(5, 4), layer = 2)
		lamp = SpriteObject(spritePath = "Images/Lamp.png", position = Vector2(-5, 4), layer = 2)

		rug = SpriteObject(spritePath = "Images/Rug.png", position = Vector2(0, -1), layer = 0)

		couches = SpriteObject(spritePath = "Images/Couches.png", position = Vector2(-12, 3), pivot = Vector2(-1, 1), layer = 2)
		tablesAndChairs = SpriteObject(spritePath = "Images/TablesAndChairs.png", position = Vector2(12, 3), pivot = Vector2(1, 1), layer = 2)

		# show all colliders for testing
		GameManager.showAllColliders()