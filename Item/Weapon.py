from abc import ABC, abstractmethod

from Item.Item import Item

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
