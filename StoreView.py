from Engine import *
from Player import Player
from Layers import Layers

# this class contains all the game objects and stuff for the scene
class StoreView:

	# this is called when the scene is opened. creates all the gameObjects it needs.
	@staticmethod
	def start():
		# create player
		player = Player()

		# store
		background = SpriteObject(spritePath = "Images/FloorAndWalls.png", size = GameManager.screenSizeWorldUnits, layer = Layers.background)		
		Collider.RectangleCollider(parent = background, pivot = Vector2(-1, 0), size = Vector2(0.25, background.size.y), offset = Vector2(-background.size.x / 2, 0), enableCollisionEvents = False)
		Collider.RectangleCollider(parent = background, pivot = Vector2(1, 0), size = Vector2(0.25, background.size.y), offset = Vector2(background.size.x / 2, 0), enableCollisionEvents = False)
		Collider.RectangleCollider(parent = background, pivot = Vector2(0, -1), size = Vector2(background.size.x, 0.25), offset = Vector2(0, -background.size.y / 2), enableCollisionEvents = False)
		Collider.RectangleCollider(parent = background, pivot = Vector2(0, 1), size = Vector2(background.size.x, 0.25), offset = Vector2(0, background.size.y / 2), enableCollisionEvents = False)

		salesTable = SpriteObject(spritePath = "Images/SalesTable.png", position = Vector2(0, 4), layer = Layers.furniture)
		Collider.RectangleCollider(parent = salesTable, pivot = Vector2(-1, 0), size = Vector2(0.25, salesTable.size.y), offset = Vector2(-salesTable.size.x / 2, 0), enableCollisionEvents = False)
		Collider.RectangleCollider(parent = salesTable, pivot = Vector2(0, 0), size = Vector2(0.5, salesTable.size.y), enableCollisionEvents = False)		
		Collider.RectangleCollider(parent = salesTable, pivot = Vector2(1, 0), size = Vector2(0.25, salesTable.size.y), offset = Vector2(salesTable.size.x / 2, 0), enableCollisionEvents = False)

		clock = SpriteObject(spritePath = "Images/Clock.png", position = Vector2(5, 4), layer = Layers.furniture)
		clockCollider = Collider.RectangleCollider(parent = clock, size = Vector2(clock.size.x - 0.35, 0.5), pivot = Vector2(0, -1), enableCollisionEvents = False)
		clockCollider.position.y -= clock.size.y / 2

		lamp = SpriteObject(spritePath = "Images/Lamp.png", position = Vector2(-5, 4), layer = Layers.furniture)
		lampCollider = Collider.RectangleCollider(parent = lamp, size = Vector2(lamp.size.x - 0.25, 0.4), pivot = Vector2(0, -1), enableCollisionEvents = False)
		lampCollider.position.y -= lamp.size.y / 2

		rug = SpriteObject(spritePath = "Images/Rug.png", position = Vector2(0, -1), layer = Layers.background)
		
		couch1 = SpriteObject(spritePath = "Images/Couch.png", position = Vector2(-12, 3), pivot = Vector2(-1, 1), layer = Layers.furniture)

		couch2 = SpriteObject(spritePath = "Images/Couch.png", position = Vector2(-12, -1), pivot = Vector2(-1, 1), layer = Layers.furniture)
		
		chouch1Collider = Collider.RectangleCollider(parent = couch1, size = Vector2(couch2.size.x - 0.1, 2.9), pivot = Vector2(0, -1), offset = Vector2(0, -couch1.size.y / 2), enableCollisionEvents = False)
		chouch2Collider = Collider.RectangleCollider(parent = couch2, size = Vector2(couch2.size.x - 0.1, 2.9), pivot = Vector2(0, -1), offset = Vector2(0, -couch2.size.y / 2), enableCollisionEvents = False)

		# TODO: create parent/grouping and cloning for game objects to make stuff like this less annoying. possibly also create an option for an entire group to be combined into a single sprite object for efficiency

		table1 = SpriteObject(spritePath = "Images/Table.png", position = Vector2(10.5, 1), pivot = Vector2(1, -1), layer = Layers.furniture, reflection = Vector2Bool(True, False))
		table1Collider = Collider.RectangleCollider(parent = table1, size = Vector2(table1.size.x, 1), pivot = Vector2(0, -1), offset = Vector2(0, -table1.size.y / 2), enableCollisionEvents = False)

		chair1 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(12, 1), pivot = Vector2(1, -1), layer = Layers.furniture, reflection = Vector2Bool(True, False))
		chair1Collider = Collider.RectangleCollider(parent = chair1, size = Vector2(1, 1), pivot = Vector2(0, -1), offset = Vector2(0, -chair1.size.y / 2), enableCollisionEvents = False)

		reflectedChair1 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(8.5, 1), pivot = Vector2(1, -1), layer = Layers.furniture)
		reflectedChair1Collider = Collider.RectangleCollider(parent = reflectedChair1, size = Vector2(1, 1), pivot = Vector2(0, -1), offset = Vector2(0, -reflectedChair1.size.y / 2), enableCollisionEvents = False)

		table2 = SpriteObject(spritePath = "Images/Table.png", position = Vector2(10.5, -2), pivot = Vector2(1, -1), layer = Layers.furniture, reflection = Vector2Bool(True, False))
		table2Collider = Collider.RectangleCollider(parent = table2, size = Vector2(table2.size.x, 1), pivot = Vector2(0, -1), offset = Vector2(0, -table2.size.y / 2), enableCollisionEvents = False)

		chair2 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(12, -2), pivot = Vector2(1, -1), layer = Layers.furniture, reflection = Vector2Bool(True, False))
		chair2ollider = Collider.RectangleCollider(parent = chair2, size = Vector2(1, 1), pivot = Vector2(0, -1), offset = Vector2(0, -chair2.size.y / 2), enableCollisionEvents = False)

		reflectedChair2 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(8.5, -2), pivot = Vector2(1, -1), layer = Layers.furniture)
		reflectedChair2Collider = Collider.RectangleCollider(parent = reflectedChair2, size = Vector2(1, 1), pivot = Vector2(0, -1), offset = Vector2(0, -reflectedChair2.size.y / 2), enableCollisionEvents = False)

		table3 = SpriteObject(spritePath = "Images/Table.png", position = Vector2(10.5, -5), pivot = Vector2(1, -1), layer = Layers.furniture, reflection = Vector2Bool(True, False))
		table3Collider = Collider.RectangleCollider(parent = table3, size = Vector2(table3.size.x, 1), pivot = Vector2(0, -1), offset = Vector2(0, -table3.size.y / 2), enableCollisionEvents = False)

		chair3 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(12, -5), pivot = Vector2(1, -1), layer = Layers.furniture, reflection = Vector2Bool(True, False))
		chair3Collider = Collider.RectangleCollider(parent = chair3, size = Vector2(1, 1), pivot = Vector2(0, -1), offset = Vector2(0, -chair3.size.y / 2), enableCollisionEvents = False)

		reflectedChair3 = SpriteObject(spritePath = "Images/Chair.png", position = Vector2(8.5, -5), pivot = Vector2(1, -1), layer = Layers.furniture)
		reflectedChair3Collider = Collider.RectangleCollider(parent = reflectedChair3, size = Vector2(1, 1), pivot = Vector2(0, -1), offset = Vector2(0, -reflectedChair3.size.y / 2), enableCollisionEvents = False)

		# show all colliders for testing
		GameManager.showAllColliders()