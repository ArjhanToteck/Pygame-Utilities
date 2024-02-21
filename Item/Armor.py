from abc import ABC, abstractmethod

from Item.Item import Item

class Armor(Item):
	BASE_PRICE = 7
	PRICE_PER_ARMOR_CLASS = 3


	def __init__(self, name, armorClass = 0, quantity = 1, icon = None, iconPath = None):
		super().__init__(name, quantity, icon, iconPath)

		self.armorClass = armorClass
		
		
	def clone(self):
		return Armor(self.name, self.armorClass, self.quantity, self.icon)
	
	
	def __str__ (self):
		return super().__str__() + f"\nArmor Class: {self.armorClass}"


	def calculatePricePerItem(self):
		price = Armor.BASE_PRICE

		# factor price for every AC point
		price += self.armorClass * Armor.PRICE_PER_ARMOR_CLASS

		return price