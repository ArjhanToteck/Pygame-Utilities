from GameManager import GameManager
from GameObject import GameObject
from SpriteObject import SpriteObject
from Vector2 import Vector2
from Vector2Bool import Vector2Bool
from Player import Player
from SpriteSheet import SpriteSheet

import Collider

# this class contains all the game objects and stuff for the scene
class StoreView:

	# this is called when the scene is opened. creates all the gameObjects it needs.
	@staticmethod
	def start():
		# create player
		player = Player()

		# store
		background = SpriteObject(spritePath = "Images/FloorAndWalls.png", size = GameManager.screenSizeWorldUnits, layer = 0)

		salesTable = SpriteObject(spritePath = "Images/SalesTable.png", position = Vector2(0, 4), layer = 2)
		Collider.RectangleCollider(parent = salesTable, pivot = Vector2(-1, 0), size = Vector2(0.25, salesTable.size.y), offset = Vector2(-salesTable.size.x / 2, 0))
		Collider.RectangleCollider(parent = salesTable, pivot = Vector2(0, 0), size = Vector2(0.5, salesTable.size.y))		
		Collider.RectangleCollider(parent = salesTable, pivot = Vector2(1, 0), size = Vector2(0.25, salesTable.size.y), offset = Vector2(salesTable.size.x / 2, 0))

		clock = SpriteObject(spritePath = "Images/Clock.png", position = Vector2(5, 4), layer = 2)
		clockCollider = Collider.RectangleCollider(parent = clock, size = Vector2(clock.size.x - 0.35, 0.5), pivot = Vector2(0, -1))
		clockCollider.position.y -= clock.size.y / 2

		lamp = SpriteObject(spritePath = "Images/Lamp.png", position = Vector2(-5, 4), layer = 2)
		lampCollider = Collider.RectangleCollider(parent = lamp, size = Vector2(lamp.size.x - 0.25, 0.4), pivot = Vector2(0, -1))
		lampCollider.position.y -= lamp.size.y / 2

		rug = SpriteObject(spritePath = "Images/Rug.png", position = Vector2(0, -1), layer = 0)

		# TODO: figure out better parameters for colliders and pivots/offsets to make things like this less annoying. maybe it should factor in both the pivot of the game object and the collider?
		couch1 = SpriteObject(spritePath = "Images/Couch.png", position = Vector2(-12, 3), pivot = Vector2(-1, 1), layer = 2)
		couch2 = SpriteObject(spritePath = "Images/Couch.png", position = Vector2(-12, -1), pivot = Vector2(-1, 1), layer = 2)

		chouch1Collider = Collider.RectangleCollider(parent = couch1, size = Vector2(couch1.size.x - 0.1, 2.9), pivot = Vector2(-1, -1))
		chouch1Collider.position.y -= couch1.size.y

		chouch2Collider = Collider.RectangleCollider(parent = couch2, size = Vector2(couch2.size.x - 0.1, 2.9), pivot = Vector2(-1, -1))
		chouch2Collider.position.y -= couch2.size.y

		#TODO: create parent/grouping and cloning for game objects to make stuff like this less annoying

		table1 = SpriteObject(spritePath = "Images/Table.png", position = Vector2(10.5, 1), pivot = Vector2(1, -1), layer = 2, reflection = Vector2Bool(True, False))
		table1Collider = Collider.RectangleCollider(parent = table1, size = (Vector2(table1.size.x, 1)))
		chair1 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(12, 1), pivot = Vector2(1, -1), layer = 2, reflection = Vector2Bool(True, False))
		chair1Collider = Collider.RectangleCollider(parent = chair1, size = (Vector2(1, 1)))
		reflectedChair1 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(8.5, 1), pivot = Vector2(1, -1), layer = 2)
		reflectedChair1Collider = Collider.RectangleCollider(parent = reflectedChair1, size = (Vector2(1, 1)))

		table2 = SpriteObject(spritePath = "Images/Table.png", position = Vector2(10.5, -2), pivot = Vector2(1, -1), layer = 2, reflection = Vector2Bool(True, False))
		table2Collider = Collider.RectangleCollider(parent = table2, size = (Vector2(table2.size.x, 1)))
		chair2 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(12, -2), pivot = Vector2(1, -1), layer = 2, reflection = Vector2Bool(True, False))
		chair2ollider = Collider.RectangleCollider(parent = chair2, size = (Vector2(1, 1)))
		reflectedChair2 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(8.5, -2), pivot = Vector2(1, -1), layer = 2)
		reflectedChair2Collider = Collider.RectangleCollider(parent = reflectedChair2, size = (Vector2(1, 1)))

		table3 = SpriteObject(spritePath = "Images/Table.png", position = Vector2(10.5, -5), pivot = Vector2(1, -1), layer = 2, reflection = Vector2Bool(True, False))
		table3Collider = Collider.RectangleCollider(parent = table3, size = (Vector2(table3.size.x, 1)))
		chair3 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(12, -5), pivot = Vector2(1, -1), layer = 2, reflection = Vector2Bool(True, False))
		chair3Collider = Collider.RectangleCollider(parent = chair3, size = (Vector2(1, 1)))
		reflectedChair3 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(8.5, -5), pivot = Vector2(1, -1), layer = 2)
		reflectedChair3Collider = Collider.RectangleCollider(parent = reflectedChair3, size = (Vector2(1, 1)))

		# show all colliders for testing
		GameManager.showAllColliders()