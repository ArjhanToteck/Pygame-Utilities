from ShopItem import ShopItem

class Weapon(ShopItem):
    def __init__(self, name, value, damage, knockback, attackModifier):
        super().__init__(name, value)
        self.damage = damage
        self.knockback = knockback
        self.attackModifier = attackModifier