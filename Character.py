from Engine import *

class Character(SpriteObject):
    def __init__(self, position=None, size=None, visible=True, layer=1, reflection=None, pivot=None, spritePath=None, sprite=None, maxHealth = 10, currentHealth = None):
        super().__init__(position, size, visible, layer, reflection, pivot, spritePath, sprite)
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