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
		# TODO: allow for different text overflow settings, ie ellipses, vertical overflow, horizontal overflow, resizetext
		# TODO: make some kind of tag system like css or unity rich text for color and stuff
		
		# split into lines with \n
		preSplitLines = self.text.split("\n")

		# create new holder for the actual lines that will be drawn
		lines = []

		# hold rendered lines
		renderedLines = []

		# size in pixels of textbox
		totalSizePixels = Vector2(0, 0)

		# loop through already split \n lines
		for i in range(len(preSplitLines)):
			preSplitLine = preSplitLines[i]
			
			# divide line further into words
			words = preSplitLine.split(" ")

			# first word will always be a new line since there was a \n before it
			lines.append(words[0])

			# loop through words
			for i in range(1, len(words)):
				word = words[i]
				
				# test if we can fit the current word in the last line
				lastLine = lines[-1]
				testLine = lastLine + " " + word
				testWidth = self.font.size(testLine)[0]

				# break up into new line if needed
				if testWidth <= self.textBoundarySize.x * GameManager.worldUnitSize.x:
					lines[-1] = testLine
				else:
					# start new line
					lines.append(word)


		def renderLine(line):
			# render last line
			renderedLine = self.font.render(line, True, self.color)
			renderedLines.append(renderedLine)

			# update dimensions
			totalSizePixels.y += renderedLine.get_height()

			currentWidth = renderedLine.get_width()

			# replace total width of current line is wider
			if currentWidth > totalSizePixels.x:
				totalSizePixels.x = currentWidth
		

		for line in lines:
			renderLine(line)

		# create combined surface
		combinedSurface = Engine.pygame.Surface(totalSizePixels.toTuple(), Engine.pygame.SRCALPHA)
		
		# place text onto combined surface
		currentHeight = 0
		for renderedLine in renderedLines:
			xPosition = 0

			# set x based on alignment
			match self.alignment:
				case Textbox.Alignment.Right:
					xPosition = totalSizePixels.x - (renderedLine.get_width())

				case Textbox.Alignment.Center:
					xPosition = (totalSizePixels.x / 2) - (renderedLine.get_width() / 2)

				# left by default
				case _:
					xPosition = 0

			# add line to combined surface
			combinedSurface.blit(renderedLine, (xPosition, currentHeight))

			# track the height we're at
			currentHeight += renderedLine.get_height()
			
		# update sprite
		self.setSizePixels(totalSizePixels)
		self.setSprite(combinedSurface)
		self.updateSpriteTransformations()


	def setText(self, text = ""):
		self.text = text
		self.renderText()