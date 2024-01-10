from ShopItem import ShopItem

class Armor(ShopItem):
    def __init__(self, name, value, armorClass):
        super().__init__(name, value)

        self.armorClass = armorClass