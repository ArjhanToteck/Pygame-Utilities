from GameManager import GameManager
from Vector2 import Vector2

# TODO: implement actual collision, allow colliders to be added to GameObjects, create subclasses for different collider types
class Collider:
    def __init__(self, parent, offset = None, position = None, isTrigger = False, followParent = True, visible = False):
        # parent gameObject
        self.parent = parent
        self.isTrigger = isTrigger
        self.followParent = followParent
        self.visible = visible # TODO: add a way to render colliders for debug

        # default offset
        if offset == None:
            offset = Vector2()

        # default position
        if position == None:
            position = parent.position + offset
            
        # add self to global collider list
        GameManager.colliders.append(self)