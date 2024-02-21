from abc import ABC, abstractmethod

from Item.Item import Item

class Consumable(Item):
	def __init__(self, name, quantity = 1, icon = None, iconPath = None):
		super().__init__(name, quantity, icon, iconPath)


	def clone(self):
		return Consumable(self.name, self.quantity, self.icon)
	

	@abstractmethod
	def calculatePricePerItem(self):
		pass