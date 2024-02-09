import Engine
from Layers import Layers
from Order import Order

class StoreMenu(Engine.Shape.Rectangle):
	
	def __init__(self, isOpen = False, items = [], color = (135, 62, 35), borderSize = 1, fill = True, visible = False, layer = Layers.ui, parent = None, position = None, size = None, pivot = None):
		super().__init__(color, borderSize, fill, visible, layer, parent, position, size, pivot)
		titleFont = Engine.pygame.font.Font("Fonts/nokiafc22.ttf", 25)

		self.isOpen = isOpen
		self.items = items
		self.storeItemBlocks = []

		self.createItemBlocks()

		if self.isOpen:
			self.open()

		self.title = Engine.Textbox(parent = self, text = "Store", size = Engine.Vector2(5, 1), font = titleFont, layer = Layers.ui, position = Engine.Vector2(0, (self.size.y / 2) - 0.5), alignment = Engine.Textbox.Alignment.Center, pivot = Engine.Vector2(0, 1), visible = False)


	class ItemBlock(Engine.Shape.Rectangle):
	
		def __init__(self, item = None, color = (54, 31, 3), borderSize = 1, fill = True, visible = True, layer = Layers.ui, parent = None, position = None, size = Engine.Vector2(1.5, 1.5), pivot = None):
			super().__init__(color, borderSize, fill, visible, layer, parent, position, size, pivot)
						
			self.item = item
			self.itemSpriteObject = Engine.SpriteObject(parent = self, sprite = self.item.icon, layer = self.layer + 1, size = self.size)
			self.buttonCollider = Engine.Collider.RectangleCollider(parent = self, layer = 999)
			self.button = Engine.Button(collider = self.buttonCollider)


	def open(self):
		self.isOpen = True

		# show stuff
		self.show()

		# reset order
		self.order = Order()
		

	def close(self):
		self.isOpen = False

		self.hide()


	def createItemBlocks(self):
		# display items
		for i in range(len(self.items)):
			item = self.items[i]
			itemBlock = StoreMenu.ItemBlock(parent = self, item = item, position = Engine.Vector2((i * 2) - 9.5, 3), visible = self.isOpen)
			self.storeItemBlocks.append(itemBlock)