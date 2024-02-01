from Engine import *

from Inventory import Inventory
from Layers import Layers
from Character import Character

import Item

# player class
# TODO: make character class to inherit from
class Player(Character):
	# load sprite sheet
	spriteSheet = SpriteSheet(imagePath = "Images/Player.png")
	
	spriteSheet.sliceByRowsAndColumns(10, 6, rowNames = ["downIdle", "sideIdle", "upIdle", "downRun", "sideRun", "upRun", "downAttack", "sideAttack", "upAttack", "death"])

	def __init__(self, speed = 5, maxHealth = 10, currentHealth = None, position = None, size = None, reflection = None, pivot = None, spritePath = None, sprite = None, visible = True, layer = 1, parent = None):
		# set defaults
		if sprite == None and spritePath == None:
			sprite = Player.spriteSheet.sprites["downIdle"][0]

		if size == None:
			size = Vector2(3, 3)

		if layer == None:
			layer = Layers.player

		# do regular character init
		super().__init__(maxHealth, currentHealth, position, size, reflection, pivot, spritePath, sprite, visible, layer, parent)

		# exclusive player properties
		self.speed = speed

		self.running = False
		self.direction = Vector2.down
		self.animationController = AnimationController(6, 0.125)

		# add inventory
		self.inventory = Inventory()
		
		# add collider to self
		self.collider = Collider.RectangleCollider(parent = self, pivot = Vector2(0, 1), size = Vector2(self.size.x / 4, self.size.y / 3), offset = Vector2(0, -0.1))

	def onUpdate(self):
		# reset running and reflection
		self.running = False
		self.reflection = Vector2Bool(False, False)

		# movement
		newDirection = Vector2.zero

		# get direction
		if GameManager.keysDown[pygame.K_DOWN]: 
			newDirection += Vector2.down

		if GameManager.keysDown[pygame.K_UP]:
			newDirection += Vector2.up

		if GameManager.keysDown[pygame.K_LEFT]:
			newDirection += Vector2.left

		if GameManager.keysDown[pygame.K_RIGHT]:
			newDirection += Vector2.right
			
		# check if there was movement
		if newDirection != Vector2.zero:
			# move in direction
			self.direction = newDirection
			self.move(self.direction * self.speed * GameManager.deltaTime)

			# mark as running
			self.running = True

		# animations
		animationRow = ""

		# account for direction
		if self.direction.x == -1:
			animationRow = "side"
			self.reflection = Vector2Bool(True, False)

		elif self.direction.x == 1:
			animationRow = "side"

		elif self.direction.y == -1:
			animationRow = "down"

		elif self.direction.y == 1:
			animationRow = "up"

		# account for running
		if self.running:
			animationRow += "Run"
		else:
			animationRow += "Idle"

		# get animation frame
		animationFrame = self.animationController.getFrame(GameManager.deltaTime)

		# update sprite
		self.updateSprite(Player.spriteSheet.sprites[animationRow][animationFrame])