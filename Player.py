from GameManager import GameManager
from SpriteObject import SpriteObject
from Vector2 import Vector2
from Vector2Bool import Vector2Bool
from SpriteSheet import SpriteSheet
import Collider

import pygame

# player class
class Player(SpriteObject):
	# load sprite sheet
	spriteSheet = SpriteSheet(imagePath = "Images/Player.png")
	# TODO: doesn't seem to be slicing things correctly. fix spritesheet slicing
	spriteSheet.sliceByRowsAndColumns(10, 6, rowNames = ["downIdle", "sideIdle", "upIdle", "downRun", "sideRun", "upRun", "downAttack", "sideAttack", "upAttack", "death"])

	def __init__(self, speed = 5, position = None, size = None, visible = True,  layer = 1, reflection = None, pivot = None, spritePath = None, sprite = None):
		# set default sprite
		if sprite == None and spritePath == None:
			sprite = Player.spriteSheet.sprites["downIdle"][0]

		if size == None:
			size = Vector2(3, 3)

		# do regular sprite init
		super().__init__(position, size, visible, layer, reflection, pivot, spritePath, sprite)

		# exclusive player properties
		self.speed = speed
		self.running = False
		self.direction = Vector2.down

		# add collider to self		
		Collider.RectangleCollider(parent = self, pivot = Vector2(0, 1), size = Vector2(self.size.x / 4, self.size.y / 3), offset = Vector2(0, -0.1))

	def onUpdate(self):
		# reset running and reflection
		self.running = False
		self.reflection = Vector2Bool(False, False)

		# movement
		newDirection = Vector2.zero

		if GameManager.keysDown[pygame.K_DOWN]: 
			self.move(Vector2(0, -self.speed * GameManager.deltaTime))
			self.running = True
			newDirection += Vector2.down

		if GameManager.keysDown[pygame.K_UP]:
			self.move(Vector2(0, self.speed * GameManager.deltaTime))
			self.running = True
			newDirection += Vector2.up

		if GameManager.keysDown[pygame.K_LEFT]:
			self.move(Vector2(-self.speed * GameManager.deltaTime, 0))
			self.running = True
			newDirection += Vector2.left

		if GameManager.keysDown[pygame.K_RIGHT]:
			self.move(Vector2(self.speed * GameManager.deltaTime, 0))
			self.running = True
			newDirection += Vector2.right

		if newDirection != Vector2.zero:
			self.direction = newDirection

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

		# update sprite
		self.updateSprite(Player.spriteSheet.sprites[animationRow][0])