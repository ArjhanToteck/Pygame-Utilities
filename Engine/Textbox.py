import Engine
from Engine.GameManager import GameManager
from Engine.Vector2 import Vector2

class Textbox(Engine.SpriteObject):
	def __init__(self, text = "", font = None, color = (255, 255, 255), reflection = None, visible = True, layer = 1, parent = None, position = None, size = None, pivot = None):
	
		self.text = text
		self.color = color
		
		if font == None:
			self.font = Engine.pygame.font.SysFont('Segoe UI', 32)
		else:
			self.font = font
					
		# do regular sprite init
		super().__init__(reflection, None, None, visible, layer, parent, position, size, pivot)

		self.renderTextSprite()


	def renderTextSprite(self):
		# TODO: allow for different alignments, ie left, right, center
		# TODO: allow for different text overflow settings, ie ellipses, vertical overflow, horizontal overflow, autosize
		words = self.text.split(" ") + [""]
		
		lines = [""]
		renderedLines = []
		totalSize = Vector2(0, 0)

		# loop through words
		for word in words:

			lastLine = lines[-1]
			testLine = lastLine + word
			testWidth = self.font.size(testLine)[0]

			# break up into new line if needed
			if testWidth <= self.size.x * GameManager.worldUnitSize.x:
				lines[-1] = testLine + " "
			else:
				# render last line
				renderedLine = self.font.render(lastLine, True, self.color)
				renderedLines.append(renderedLine)

				# update dimensions
				totalSize.y += renderedLine.get_height()
				print(renderedLine.get_height())

				currentWidth = renderedLine.get_width()

				# replace total width of current line is wider
				if currentWidth > totalSize.x:
					totalSize.x = currentWidth	

				# start new line
				lines.append(word)
				
		# create combined surface
		combinedSurface = Engine.pygame.Surface(totalSize.toTuple(), Engine.pygame.SRCALPHA)
		
		# place text onto combined surface
		currentHeight = 0
		for renderedLine in renderedLines:
			combinedSurface.blit(renderedLine, (0, currentHeight))
			currentHeight += renderedLine.get_height()
			
		# update sprite
		# TODO: find a way to do this without having to change the size property. might need to make a custom onRender function
		self.setSizePixels(totalSize)
		self.setSprite(combinedSurface)


	def setText(self, text = ""):
		self.text = text
		self.renderText()