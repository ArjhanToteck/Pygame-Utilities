import Engine
from Engine.GameManager import GameManager
from Engine.Vector2 import Vector2
from Layers import Layers

from enum import Enum

class Textbox(Engine.SpriteObject):
	# enum for alignments
	class Alignment(Enum):
		Left = 0
		Center = 1
		Right = 2

	
	def __init__(self, text = "", font = None, color = (255, 255, 255), alignment = None, textBoundarySize = None, reflection = None, visible = True, layer = Layers.ui, parent = None, position = None, size = None, pivot = None):
		# do regular sprite init
		super().__init__(reflection, None, None, visible, layer, parent, position, size, pivot)

		self.text = text
		self.color = color
		
		if font == None:
			self.font = Engine.pygame.font.SysFont('Segoe UI', 32)
		else:
			self.font = font

		if alignment == None:
			self.alignment = Textbox.Alignment.Left
		else:
			self.alignment = alignment

		if textBoundarySize == None:
			self.textBoundarySize = size
		else:
			self.textBoundarySize = textBoundarySize
					
		self.renderTextSprite()
		

	def renderTextSprite(self):
		# TODO: allow for different alignments, ie left, right, center
		# TODO: allow for different text overflow settings, ie ellipses, vertical overflow, horizontal overflow, autosize
		words = self.text.split(" ")
		
		lines = [words[0]]
		renderedLines = []
		totalSize = Vector2(0, 0)

		def renderLine(line):
			# render last line
			renderedLine = self.font.render(line, True, self.color)
			renderedLines.append(renderedLine)

			# update dimensions
			totalSize.y += renderedLine.get_height()

			currentWidth = renderedLine.get_width()

			# replace total width of current line is wider
			if currentWidth > totalSize.x:
				totalSize.x = currentWidth	

		# loop through words
		for i in range(1, len(words)):			
			word = words[i]

			lastLine = lines[-1]
			testLine = lastLine + " " + word
			testWidth = self.font.size(testLine)[0]

			# break up into new line if needed
			if testWidth <= self.textBoundarySize.x * GameManager.worldUnitSize.x:
				lines[-1] = testLine
			else:
				# start new line
				lines.append(word)

		for line in lines:
			renderLine(line)

		# create combined surface
		combinedSurface = Engine.pygame.Surface(totalSize.toTuple(), Engine.pygame.SRCALPHA)
		
		# place text onto combined surface
		currentHeight = 0
		for renderedLine in renderedLines:
			xPosition = 0

			# set x based on alignment
			match self.alignment:
				case Textbox.Alignment.Right:
					xPosition = totalSize.x - (renderedLine.get_width())

				case Textbox.Alignment.Center:
					xPosition = (totalSize.x / 2) - (renderedLine.get_width() / 2)

				# left by default
				case _:
					xPosition = 0

			# add line to combined surface
			combinedSurface.blit(renderedLine, (xPosition, currentHeight))

			# track the height we're at
			currentHeight += renderedLine.get_height()
			
		# update sprite
		self.setSizePixels(totalSize)
		self.setSprite(combinedSurface)
		self.updateSpriteTransformations()


	def setText(self, text = ""):
		self.text = text
		self.renderText()