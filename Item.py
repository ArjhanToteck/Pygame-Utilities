from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name):
        self.name = name


    def onUse(self, character):
        pass


    def __str__ (self):
        return "Item " + self.name


    # TODO: implement this on everything
    #@abstractmethod
    def calculateCost(self):
        pass


    def calculateTax(self, taxPercent = 0.0725):
        return self.calculateCost() * taxPercent

# comsumables

class Consumable(Item):
    def __init__(self, name):
        super().__init__(name)


class HealthPotion(Consumable):
    def __init__(self, name, health):
        super().__init__(name)
        self.health = health


    def onUse(self, character):
        character.heal(self.health)

# HealthPotion should be accessable through Consumable.HealthPotion
Consumable.HealthPotion = HealthPotion

# weapons

class Weapon(Item):
    def __init__(self, name, damage, knockback, attackModifier = 0):
        super().__init__(name)
        self.damage = damage
        self.knockback = knockback
        self.attackModifier = attackModifier


# armor
class Armor(Item):
    def __init__(self, name, armorClass):
        super().__init__(name)

        self.armorClass = armorClass