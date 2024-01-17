class ShopItem:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def onUse(self, character):
        pass
# comsumables

class Consumable(ShopItem):
    def __init__(self, name, value):
        super().__init__(name, value)

class HealthPotion(Consumable):
    def __init__(self, name, value, health):
        super().__init__(name, value)
        self.health = health

    def onUse(self, character):
        character.heal(self.health)

# HealthPotion should be accessable through Consumable.HealthPotion
Consumable.HealthPotion = HealthPotion

# weapons

class Weapon(ShopItem):
    def __init__(self, name, value, damage, knockback, attackModifier):
        super().__init__(name, value)
        self.damage = damage
        self.knockback = knockback
        self.attackModifier = attackModifier

# armor

class Armor(ShopItem):
    def __init__(self, name, value, armorClass):
        super().__init__(name, value)

        self.armorClass = armorClass