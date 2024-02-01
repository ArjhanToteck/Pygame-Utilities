from Engine import *

class Character(SpriteObject):
    def __init__(self, maxHealth = 10, currentHealth = None, reflection = None, spritePath = None, sprite = None, visible = True, layer = 1, parent = None, position = None, size = None, pivot = None):
        # do regular sprite init
        super().__init__(reflection, spritePath, sprite, visible, layer, parent, position, size, pivot)

        # set fields
        self.maxHealth = maxHealth

        # maxHealth is same as health by default
        if currentHealth == None:
            self.currentHealth = self.maxHealth
        else:
            self.currentHealth = currentHealth


    def takeDamage(self, damage):
        # decrease health
        self.currentHealth -= damage

        # check for death
        if self.currentHealth <= 0:
            self.die()


    def heal(self, amount, goOverMax = False):
        self.currentHealth += amount

        # check if over max health and not supposed to
        if self.currentHealth > self.maxHealth and not goOverMax:
            self.currentHealth = self.maxHealth
                

    def die(self):
        pass