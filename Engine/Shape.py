import Engine

from Layers import Layers

class Shape(Engine.RenderedComponent):
    # TODO: make a color class. i hate magic tuples.
	def __init__(self, color = (255, 255, 255), borderSize = 1, fill = True, visible = True, layer = Layers.default, parent = None, position = None, size = None, pivot = None):
		super().__init__(visible, layer, parent, position, size, pivot)

		self.color = color
		self.borderSize = borderSize
		self.fill = fill


class Rectangle(Shape):
	def onRender(self):
		if self.visible:
			# get screen position of collider with pivot and pivot offset factored in
			screenPosition = Engine.GameManager.worldToScreenPosition(self.position + self.getPivotOffset())

			passedBorderSize = self.borderSize
   
			shape = None
   
			if self.fill:
				shape = Engine.pygame.draw.rect(Engine.GameManager.screen, self.color, Engine.pygame.Rect(screenPosition.x, screenPosition.y, self.size.x * Engine.GameManager.worldUnitSize.x, self.size.y * Engine.GameManager.worldUnitSize.y))
			else:
				shape = Engine.pygame.draw.rect(Engine.GameManager.screen, self.color, Engine.pygame.Rect(screenPosition.x, screenPosition.y, self.size.x * Engine.GameManager.worldUnitSize.x, self.size.y * Engine.GameManager.worldUnitSize.y), passedBorderSize)


Shape.Rectangle = Rectangle