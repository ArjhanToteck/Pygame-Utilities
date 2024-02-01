from Engine import *

from Player import Player
from Layers import Layers
from Order import Order
import Item

# this class contains all the game objects and stuff for the scene
class StoreView:

	# this is called when the scene is opened. creates all the components it needs.
	@staticmethod
	def start():
		# create player
		player = Player()


		# store

		# background
		# TODO: figure out a way to do internal colliders
		background = SpriteObject(spritePath = "Images/FloorAndWalls.png", size = GameManager.screenSizeWorldUnits, layer = Layers.background)		
		Collider.RectangleCollider(parent = background, pivot = Vector2(-1, 0), size = Vector2(0.25, background.size.y), offset = Vector2(-background.size.x / 2, 0), enableCollisionEvents = False)
		Collider.RectangleCollider(parent = background, pivot = Vector2(1, 0), size = Vector2(0.25, background.size.y), offset = Vector2(background.size.x / 2, 0), enableCollisionEvents = False)
		Collider.RectangleCollider(parent = background, pivot = Vector2(0, -1), size = Vector2(background.size.x, 0.25), offset = Vector2(0, -background.size.y / 2), enableCollisionEvents = False)
		Collider.RectangleCollider(parent = background, pivot = Vector2(0, 1), size = Vector2(background.size.x, 0.25), offset = Vector2(0, background.size.y / 2), enableCollisionEvents = False)

		# sales table
		salesTable = SpriteObject(spritePath = "Images/SalesTable.png", position = Vector2(0, 4), layer = Layers.furniture)
		Collider.RectangleCollider(parent = salesTable, pivot = Vector2(-1, 0), size = Vector2(0.25, salesTable.size.y), offset = Vector2(-salesTable.size.x / 2, 0), enableCollisionEvents = False)
		Collider.RectangleCollider(parent = salesTable, pivot = Vector2(0, 0), size = Vector2(0.5, salesTable.size.y), enableCollisionEvents = False)		
		Collider.RectangleCollider(parent = salesTable, pivot = Vector2(1, 0), size = Vector2(0.25, salesTable.size.y), offset = Vector2(salesTable.size.x / 2, 0), enableCollisionEvents = False)
		
		shopkeep = SpriteObject(spritePath = "Images/Shopkeep.png", size = Vector2(3, 3), layer = Layers.characters, position = Vector2(0, 5))
		
		clock = SpriteObject(spritePath = "Images/Clock.png", position = Vector2(5, 4), layer = Layers.furniture)
		clockCollider = Collider.RectangleCollider(parent = clock, size = Vector2(clock.size.x - 0.35, 0.5), pivot = Vector2(0, -1), enableCollisionEvents = False)
		clockCollider.position.y -= clock.size.y / 2

		lamp = SpriteObject(spritePath = "Images/Lamp.png", position = Vector2(-5, 4), layer = Layers.furniture)
		lampCollider = Collider.RectangleCollider(parent = lamp, size = Vector2(lamp.size.x - 0.25, 0.4), pivot = Vector2(0, -1), enableCollisionEvents = False)
		lampCollider.position.y -= lamp.size.y / 2

		rug = SpriteObject(spritePath = "Images/Rug.png", position = Vector2(0, -1), layer = Layers.background)
		
		# couches

		couch1 = SpriteObject(spritePath = "Images/Couch.png", position = Vector2(-12, 3), pivot = Vector2(-1, 1), layer = Layers.furniture)
		Collider.RectangleCollider(parent = couch1, size = Vector2(couch1.size.x - 0.1, 2.9), pivot = Vector2(0, -1), offset = Vector2(0, -couch1.size.y / 2), enableCollisionEvents = False)

		couch2 = couch1.instantiate(position = Vector2(-12, -1))
		
		# tables and chairs

		tableAndChairs1 = Component(position = Vector2(10.5, 1))

		table1 = SpriteObject(parent = tableAndChairs1, spritePath = "Images/Table.png", position = Vector2(10.5, 1), pivot = Vector2(1, -1), layer = Layers.furniture, reflection = Vector2Bool(True, False))
		Collider.RectangleCollider(parent = table1, size = Vector2(table1.size.x, 1), pivot = Vector2(0, -1), offset = Vector2(0, -table1.size.y / 2), enableCollisionEvents = False)

		chair1 = SpriteObject(parent = tableAndChairs1, spritePath = "Images/Chair.png", position = Vector2(12, 1), pivot = Vector2(1, -1), layer = Layers.furniture, reflection = Vector2Bool(True, False))
		Collider.RectangleCollider(parent = chair1, size = Vector2(1, 1), pivot = Vector2(0, -1), offset = Vector2(0, -chair1.size.y / 2), enableCollisionEvents = False)

		reflectedChair1 = chair1.instantiate(parent = tableAndChairs1, position = Vector2(8.5, 1))
		reflectedChair1.setReflection(Vector2Bool(False, False))
		
		tableAndChairs2 = tableAndChairs1.instantiate(position = Vector2(10.5, -2))
		tableAndChairs2 = tableAndChairs1.instantiate(position = Vector2(10.5, -5))
		
		# show all colliders for testing
		GameManager.showAllColliders()
 
		# test for order class
		order = Order()
		order.add(Item.Weapon("+2 Longsword", 10, 5, 2))
		order.add(Item.Weapon("Comically Large Spoon", 2, 10))
		order.add(Item.Consumable.HealthPotion("Health Potion", 2, 5))
		order.add(Item.Armor("Gold Armor", 8))

		print("order items:", order.items)

		for item in order:
			print(item)