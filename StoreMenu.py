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
		self.order = Order()
		self.storeItemBlocks = []
		self.orderItemBlocks = []

		self.selectedBlock = None

		self.createItemBlocks()

		if self.isOpen:
			self.open()

		self.title = Engine.Textbox(parent = self, text = "Store", size = Engine.Vector2(5, 1), font = self.titleFont, layer = Layers.ui, position = Engine.Vector2(0, (self.size.y / 2) - 0.5), alignment = Engine.Textbox.Alignment.Center, pivot = Engine.Vector2(0, 1), visible = False)
		self.itemsHeading = Engine.Textbox(parent = self, text = "Available Items", size = Engine.Vector2(5, 1), font = self.font, layer = Layers.ui, position = Engine.Vector2(-10.25, self.title.position.y - 0.25), pivot = Engine.Vector2(-1, 1), visible = False)
		self.orderHeading = Engine.Textbox(parent = self, text = "Order", size = Engine.Vector2(5, 1), font = self.font, layer = Layers.ui, position = Engine.Vector2(-10.25, self.itemsHeading.position.y - 3), pivot = Engine.Vector2(-1, 1), visible = False)
		self.overview = Engine.Textbox(parent = self, text = "Add items to see order summary", size = Engine.Vector2(7, 1), font = self.font, layer = Layers.ui, position = Engine.Vector2(2, 3), pivot = Engine.Vector2(-1, 1), visible = False)

		# check out button
		self.checkOutBox = Engine.Shape.Rectangle(parent = self, color = (54, 31, 3), layer = Layers.ui, size = Engine.Vector2(4, 1), position = Engine.Vector2(7, -4))
		Engine.Textbox(parent = self.checkOutBox, text = "Check out", font = self.font, layer = Layers.ui, size = Engine.Vector2(4, 1))
		self.checkOutCollider = Engine.Collider.RectangleCollider(parent = self.checkOutBox, isTrigger = True, enabled = False, layer = 999, enableCollisionEvents = False)
		self.checkOutButton = Engine.Button(collider = self.checkOutCollider)
		self.checkOutButton.onClick = self.close

	class ItemBlock(Engine.Shape.Rectangle):
	
		def __init__(self, item = None, color = (54, 31, 3), borderSize = 1, fill = True, visible = True, layer = Layers.ui, parent = None, position = None, size = Engine.Vector2(1.5, 1.5), pivot = None):
			super().__init__(color, borderSize, fill, visible, layer, parent, position, size, pivot)
						
			self.item = item
			self.itemSpriteObject = Engine.SpriteObject(parent = self, sprite = self.item.icon, layer = self.layer + 1, size = self.size)
			

		def showProperties(self):
			self.parent.overview.setText(self.item.toString())


	class PurchasableItemBlock(ItemBlock):
		def __init__(self, item = None, color = (54, 31, 3), borderSize = 1, fill = True, visible = True, layer = Layers.ui, parent = None, position = None, size = Engine.Vector2(1.5, 1.5), pivot = None):
			super().__init__(item, color, borderSize, fill, visible, layer, parent, position, size, pivot)

			self.buttonCollider = Engine.Collider.RectangleCollider(parent = self, isTrigger = True, enabled = False, layer = 999, enableCollisionEvents = False)
			self.button = Engine.Button(collider = self.buttonCollider)
			self.button.onMouseHover = self.showProperties
			self.button.onClick = self.onClick
			self.button.onMouseExit = self.onMouseExit


		def hide(self, hiddenByParent = False):
			super().hide(hiddenByParent)

			# make sure we disable colliders after hiding menu
			self.buttonCollider.enabled = False


		def show(self, overrideParentVisibility = False):
			super().show(overrideParentVisibility)

			# make sure we reenable colliders after hiding menu
			self.buttonCollider.enabled = True


		def onClick(self):
			self.parent.order.addItem(self.item.clone())
			self.parent.renderOrder()


		def onMouseExit(self):
			if len(self.parent.order) > 0:
				self.parent.overview.setText(self.parent.order.toString())
			else:
				self.parent.overview.setText("Add items to see order summary")


	def open(self):
		self.isOpen = True

		# reset overview text
		self.overview.setText("Add items to see order summary")

		# show stuff
		self.show()

		self.checkOutCollider.enabled = True
		

	def close(self):
		# reset order
		self.order = Order()
		self.renderOrder()

		self.isOpen = False

		self.checkOutCollider.enabled = False

		self.hide()

	def createItemBlocks(self):
		# display items
		for i in range(len(self.items)):
			item = self.items[i]
			itemBlock = StoreMenu.PurchasableItemBlock(parent = self, item = item, position = Engine.Vector2((i * 2) - 9.5, 3), visible = self.isOpen)
			self.storeItemBlocks.append(itemBlock)


	def renderOrder(self):
		# delete old item blocks
		for itemBlock in self.orderItemBlocks:
			itemBlock.destroy()
		self.orderItemBlocks = []

		# go and render all item blocks
		for i in range(len(self.order)):
			stack = self.order[i]
			itemBlock = StoreMenu.ItemBlock(parent = self, item = stack, position = Engine.Vector2((i * 2) - 9.5, 0))
			self.orderItemBlocks.append(itemBlock)