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


# comsumables
class Consumable(Item):
	def __init__(self, name, quantity = 1, icon = None, iconPath = None):
		super().__init__(name, quantity, icon, iconPath)


	def clone(self):
		return Consumable(self.name, self.quantity, self.icon)
	

	@abstractmethod
	def calculatePricePerItem(self):
		pass


class _HealthPotion(Consumable):
	BASE_PRICE = 5
	PRICE_PER_HP = 2

	def __init__(self, name = "Health Potion", health = 0, quantity = 1, icon = None, iconPath = None):
		super().__init__(name, quantity, icon, iconPath)
		self.health = health

		
	def clone(self):
		return _HealthPotion(self.name, self.health, self.quantity, self.icon)
	
	
	def __str__ (self):
		return super().__str__() + f"\nHealth: {self.health}"


	def onUse(self, character):
		character.heal(self.health)


	def calculatePricePerItem(self):
		price = _HealthPotion.BASE_PRICE
		price += self.health * _HealthPotion.PRICE_PER_HP

		return price
	

# HealthPotion should be accessable through Consumable.HealthPotion
Consumable.HealthPotion = _HealthPotion

# weapons
class Weapon(Item):
	BASE_PRICE = 5
	PRICE_PER_DAMAGE = 5
	PRICE_PER_KNOCKBACK = 5
	PRICE_PER_ATTACK_MODIFIER = 5


	def __init__(self, name, damage = 0, knockback = 0, attackModifier = 0, quantity = 1, icon = None, iconPath = None):
		super().__init__(name, quantity, icon, iconPath)
		self.damage = damage
		self.knockback = knockback
		self.attackModifier = attackModifier
				

	def clone(self):
		return Weapon(self.name, self.damage, self.knockback, self.attackModifier, self.quantity, self.icon)
	
	
	def __str__ (self):
		return super().__str__() + f"\nDamage: {self.damage}\nKnockback: {self.knockback}\nAttackModifier: {self.damage}"


	def calculatePricePerItem(self):
		price = Weapon.BASE_PRICE
		price += self.damage * Weapon.PRICE_PER_DAMAGE
		price += self.knockback * Weapon.PRICE_PER_KNOCKBACK
		price += self.attackModifier * Weapon.PRICE_PER_ATTACK_MODIFIER

		return price


# armor
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