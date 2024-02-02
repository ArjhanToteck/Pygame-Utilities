import Engine

class Textbox(Engine.SpriteObject):
	def __init__(self, text = "", font = None, color = (255, 255, 255), reflection = None, visible = True, layer = 1, parent = None, position = None, size = None, pivot = None):
	
		self.text = text
		self.color = color
		
		if font == None:
			self.font = Engine.pygame.font.SysFont('Segoe UI',  32)
		else:
			self.font = font

		self.renderTextSprite()
		
		# do regular sprite init
		super().__init__(reflection, None, self.sprite, visible, layer, parent, position, size, pivot)


	def renderTextSprite(self):
		self.sprite = self.font.render(self.text, True, self.color)


	def setText(self, text = ""):
		self.text = text
		self.renderText()