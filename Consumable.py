from ShopItem import ShopItem

class Consumable(ShopItem):
    def __init__(self, name, value):
        super().__init__(name, value)

# HealthPotion should be accessable through Consumable.HealthPotion, so it is in the same file
class HealthPotion(Consumable):
    def __init__(self, name, value, health):
        super().__init__(name, value)
        self.health = health

    def onUse(self, character):
        character.heal(self.health)