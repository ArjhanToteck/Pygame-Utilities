import Engine
from Layers import Layers
from Order import Order

class StoreMenu(Engine.Shape.Rectangle):
	
	def __init__(self, font, titleFont, isOpen = False, items = [], color = (135, 62, 35), borderSize = 1, fill = True, visible = False, layer = Layers.ui, parent = None, position = None, size = None, pivot = None):
		super().__init__(color, borderSize, fill, visible, layer, parent, position, size, pivot)
		self.font = font
		self.titleFont = titleFont
		self.isOpen = isOpen
		self.items = items
		self.storeItemBlocks = []

		self.createItemBlocks()

		if self.isOpen:
			self.open()

		self.title = Engine.Textbox(parent = self, text = "Store", size = Engine.Vector2(5, 1), font = self.titleFont, layer = Layers.ui, position = Engine.Vector2(0, (self.size.y / 2) - 0.5), alignment = Engine.Textbox.Alignment.Center, pivot = Engine.Vector2(0, 1), visible = False)
		self.overview = Engine.Textbox(parent = self, text = "Hover over an item to inspect", size = Engine.Vector2(7, 1), font = self.font, layer = Layers.ui, position = Engine.Vector2(2, 3), alignment = Engine.Textbox.Alignment.Left, pivot = Engine.Vector2(-1, 1), visible = False)


	class ItemBlock(Engine.Shape.Rectangle):
	
		def __init__(self, item = None, color = (54, 31, 3), borderSize = 1, fill = True, visible = True, layer = Layers.ui, parent = None, position = None, size = Engine.Vector2(1.5, 1.5), pivot = None):
			super().__init__(color, borderSize, fill, visible, layer, parent, position, size, pivot)
						
			self.item = item
			self.itemSpriteObject = Engine.SpriteObject(parent = self, sprite = self.item.icon, layer = self.layer + 1, size = self.size)
			self.buttonCollider = Engine.Collider.RectangleCollider(parent = self, isTrigger = True, enabled = False, layer = 999)
			self.button = Engine.Button(collider = self.buttonCollider)
			self.button.onMouseHover = self.showProperties
			self.button.onClick = self.onClick

		
		def hide(self, hiddenByParent = False):
			super().hide(hiddenByParent)

			# make sure we disable colliders after hiding menu
			self.buttonCollider.enabled = False


		def show(self, overrideParentVisibility = False):
			super().show(overrideParentVisibility)

			# make sure we reenable colliders after hiding menu
			self.buttonCollider.enabled = True


		def showProperties(self):
			self.parent.overview.setText(self.item.toString())


		def onClick(self):
			print("balls")


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