from abc import ABC, abstractmethod

from Item.Consumable import Consumable

class HealthPotion(Consumable):
	BASE_PRICE = 5
	PRICE_PER_HP = 2

	def __init__(self, name = "Health Potion", health = 0, quantity = 1, icon = None, iconPath = None):
		super().__init__(name, quantity, icon, iconPath)
		self.health = health

		
	def clone(self):
		return HealthPotion(self.name, self.health, self.quantity, self.icon)
	
	
	def __str__ (self):
		return super().__str__() + f"\nHealth: {self.health}"


	def onUse(self, character):
		character.heal(self.health)


	def calculatePricePerItem(self):
		price = HealthPotion.BASE_PRICE
		price += self.health * HealthPotion.PRICE_PER_HP

		return price
	
