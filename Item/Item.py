from abc import ABC, abstractmethod

import Engine

class Item(ABC):
	TAX_PERCENT = 0.0725


	def __init__(self, name, quantity = 1, icon = None, iconPath = None):
		self.name = name
		self.quantity = quantity
		
		# load icon from path if applicable
		if iconPath != None:
			self.icon = Engine.pygame.image.load(iconPath)

		if icon != None:
			self.icon = icon


	def clone(self):
		return Item(self.name, self.quantity, self.icon)


	def onUse(self, character):
		pass


	def __str__ (self):
		return f"{self.name} x{self.quantity}.\nPrice per unit: {self.calculatePricePerItem()}\nTotal cost: {self.calculateTotalPrice()}\nTotal tax: {self.calculateTax() * self.quantity}"


	def toString(self):
		return self.__str__()


	# TODO: implement this on everything
	@abstractmethod
	def calculatePricePerItem(self):
		pass


	def calculateTotalPrice(self):
		return self.calculatePricePerItem() * self.quantity


	# taxes in a video game is actually insane why are we adding this bruh
	def calculateTax(self):
		return self.calculatePricePerItem() * Item.TAX_PERCENT


	def calculateTotalTax(self):
		return self.calculateTax() * self.quantity