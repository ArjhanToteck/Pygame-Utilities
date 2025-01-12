import Engine

from Player import Player
from Layers import Layers
from Order import Order
from StoreMenu import StoreMenu

from Item.Armor import Armor
from Item.Weapon import Weapon
from Item.HealthPotion import HealthPotion

# this class contains all the game objects and stuff for the scene
class StoreView:
	storeSize = Engine.Vector2(25.5, 14.5)

	# this is called when the scene is opened. creates all the components it needs.
	@staticmethod
	def start():
		titleFont = Engine.pygame.font.Font("Fonts/nokiafc22.ttf", 25)
		font = Engine.pygame.font.Font("Fonts/nokiafc22.ttf", 18)

		# create player
		player = Player()

		# store

		# background
		# TODO: figure out a way to do internal colliders
		background = Engine.SpriteObject(spritePath = "Images/FloorAndWalls.png", size = StoreView.storeSize, layer = Layers.background)		
		Engine.Collider.RectangleCollider(parent = background, pivot = Engine.Vector2(-1, 0), size = Engine.Vector2(0.25, background.size.y), offset = Engine.Vector2(-background.size.x / 2, 0), enableCollisionEvents = False)
		Engine.Collider.RectangleCollider(parent = background, pivot = Engine.Vector2(1, 0), size = Engine.Vector2(0.25, background.size.y), offset = Engine.Vector2(background.size.x / 2, 0), enableCollisionEvents = False)
		Engine.Collider.RectangleCollider(parent = background, pivot = Engine.Vector2(0, -1), size = Engine.Vector2(background.size.x, 0.25), offset = Engine.Vector2(0, -background.size.y / 2), enableCollisionEvents = False)
		Engine.Collider.RectangleCollider(parent = background, pivot = Engine.Vector2(0, 1), size = Engine.Vector2(background.size.x, 0.25), offset = Engine.Vector2(0, background.size.y / 2), enableCollisionEvents = False)

		# couches

		couch1 = Engine.SpriteObject(spritePath = "Images/Couch.png", position = Engine.Vector2(-12, 3), pivot = Engine.Vector2(-1, 1), layer = Layers.furniture)
		Engine.Collider.RectangleCollider(parent = couch1, size = Engine.Vector2(couch1.size.x - 0.1, 2.9), pivot = Engine.Vector2(0, -1), offset = Engine.Vector2(0, -couch1.size.y / 2), enableCollisionEvents = False)

		couch2 = couch1.instantiate(position = Engine.Vector2(-12, -1))
		
		# tables and chairs

		tableAndChairs1 = Engine.Component(position = Engine.Vector2(10.5, 1))

		table1 = Engine.SpriteObject(parent = tableAndChairs1, spritePath = "Images/Table.png", position = Engine.Vector2(10.5, 1), pivot = Engine.Vector2(1, -1), layer = Layers.furniture, reflection = Engine.Vector2Bool(True, False))
		Engine.Collider.RectangleCollider(parent = table1, size = Engine.Vector2(table1.size.x, 1), pivot = Engine.Vector2(0, -1), offset = Engine.Vector2(0, -table1.size.y / 2), enableCollisionEvents = False)

		chair1 = Engine.SpriteObject(parent = tableAndChairs1, spritePath = "Images/Chair.png", position = Engine.Vector2(12, 1), pivot = Engine.Vector2(1, -1), layer = Layers.furniture, reflection = Engine.Vector2Bool(True, False))
		Engine.Collider.RectangleCollider(parent = chair1, size = Engine.Vector2(1, 1), pivot = Engine.Vector2(0, -1), offset = Engine.Vector2(0, -chair1.size.y / 2), enableCollisionEvents = False)

		reflectedChair1 = chair1.instantiate(parent = tableAndChairs1, position = Engine.Vector2(8.5, 1))
		reflectedChair1.setReflection(Engine.Vector2Bool(False, False))
		
		tableAndChairs2 = tableAndChairs1.instantiate(position = Engine.Vector2(10.5, -2))
		tableAndChairs2 = tableAndChairs1.instantiate(position = Engine.Vector2(10.5, -5))
  
		# sales table
		shopkeep = Engine.SpriteObject(spritePath = "Images/Shopkeep.png", size = Engine.Vector2(3, 3), layer = Layers.characters, position = Engine.Vector2(0, 5))
		
		salesTable = Engine.SpriteObject(spritePath = "Images/SalesTable.png", position = Engine.Vector2(0, 4), layer = Layers.furniture)
		Engine.Collider.RectangleCollider(parent = salesTable, pivot = Engine.Vector2(-1, 0), size = Engine.Vector2(0.25, salesTable.size.y), offset = Engine.Vector2(-salesTable.size.x / 2, 0), enableCollisionEvents = False)
		Engine.Collider.RectangleCollider(parent = salesTable, size = Engine.Vector2(0.5, salesTable.size.y), enableCollisionEvents = False)		
		Engine.Collider.RectangleCollider(parent = salesTable, pivot = Engine.Vector2(1, 0), size = Engine.Vector2(0.25, salesTable.size.y), offset = Engine.Vector2(salesTable.size.x / 2, 0), enableCollisionEvents = False)
		
		# sales trigger
		salesTrigger = Engine.Collider.RectangleCollider(parent = salesTable, size = salesTable.size + Engine.Vector2(0.5, 0.5), isTrigger = True)
		salesTextbox = Engine.Textbox(parent = salesTable, text = "Press Space to interact", size = Engine.Vector2(5, 1), font = font, layer = Layers.ui, alignment = Engine.Textbox.Alignment.Center, pivot = Engine.Vector2(0, 1), visible = False)
		salesTextbox.move(Engine.Vector2(0, -1))

		clock = Engine.SpriteObject(spritePath = "Images/Clock.png", position = Engine.Vector2(5, 4), layer = Layers.furniture)
		clockCollider = Engine.Collider.RectangleCollider(parent = clock, size = Engine.Vector2(clock.size.x - 0.35, 0.5), pivot = Engine.Vector2(0, -1), enableCollisionEvents = False)
		clockCollider.position.y -= clock.size.y / 2

		lamp = Engine.SpriteObject(spritePath = "Images/Lamp.png", position = Engine.Vector2(-5, 4), layer = Layers.furniture)
		lampCollider = Engine.Collider.RectangleCollider(parent = lamp, size = Engine.Vector2(lamp.size.x - 0.25, 0.4), pivot = Engine.Vector2(0, -1), enableCollisionEvents = False)
		lampCollider.position.y -= lamp.size.y / 2

		rug = Engine.SpriteObject(spritePath = "Images/Rug.png", position = Engine.Vector2(0, -1), layer = Layers.background)
		
		# store menu
		storeMenu = StoreMenu(font, titleFont, size = StoreView.storeSize - Engine.Vector2(4, 4), items = [
			Weapon("Fist of Ardor", 10, 5, 2, iconPath = "Images/FistOfArdor.png"),
			Weapon("Comically Large Spoon", 2, 10, iconPath = "Images/ComicallyLargeSpoon.png"),
			HealthPotion("Health Potion", 2, 5, iconPath = "Images/HealthPotion.png"),
			Armor("Gold Armor", 8, iconPath = "Images/GoldArmor.png")
		])

		# events to open store menu
		def showTextbox(collision):
			if collision.otherCollider.parent == player:
				salesTextbox.show()


		def hideTextbox(collision):
			if collision.otherCollider.parent == player:
				salesTextbox.hide()


		def salesTriggerKeyCheck(collision):
			if collision.otherCollider.parent == player:
				# check if space is down
				# TODO: implement a way in the engine to check for key press rather than being down
				try:
					if not storeMenu.isOpen and Engine.GameManager.keysPressed[Engine.pygame.key.key_code("space")]:
						salesTextbox.hide()
						storeMenu.open()
					elif storeMenu.isOpen and Engine.GameManager.keysPressed[Engine.pygame.key.key_code("escape")]:
						salesTextbox.show()
						storeMenu.close()
				except:
					pass


		salesTrigger.onTriggerEnter = showTextbox
		salesTrigger.onTriggerExit = hideTextbox
		salesTrigger.onTriggerStay = salesTriggerKeyCheck
  
		# show all colliders for debug
		Engine.GameManager.showAllColliders()