from GameManager import GameManager
from Vector2 import Vector2

# TODO: implement actual collision, allow colliders to be added to GameObjects, create subclasses for different collider types

# this is a default collider class not meant for actual use outside of being inherited by the real types of colliders
class Collider:
    def __init__(self, parent, offset = None, position = None, enabled = True, isTrigger = False, followParent = True, visible = False):
        # parent gameObject
        self.parent = parent
        self.enabled = enabled
        self.isTrigger = isTrigger
        self.followParent = followParent

        self.visible = visible # TODO: add a way to render colliders for debug (in non-default colliders)

        if(visible):
            self.show()

        # default offset
        if offset == None:
            offset = Vector2()

        # default position
        if position == None:
            position = parent.position + offset
            
        # add self to global collider list
        GameManager.colliders.append(self)


    def show(self):
        pass


    def hide(self):
        pass


    def destroy(self):
        # remove self from global collider list
        GameManager.colliders.remove(self)

        # remove self from parent
        self.parent.colliders.remove(self)
        
		# make sure not to be rendered
        self.hide()

    def checkCollisions(self):
        pass

class CollisionData:
    # enum for collision types
    class CollisionType:
        none = 0
        trigger = 1
        collision = 2

class RectangleCollider(Collider):
    def __init__(self, parent, offset=None, size = None, position=None, enabled=True, isTrigger=False, followParent=True, visible=False):
        
        # set default size
        if size == None:
            # by default, match parent size
            self.size = Vector2(parent.size.x, parent.size.y)
        else:
            self.size = size

        # call base init
        super().__init__(parent, offset, position, enabled, isTrigger, followParent, visible)

    def checkCollisions(self):
        pass

    def show(self):
        pass

    def hide(self):
        pass


class CircleCollider(Collider):
    pass


class ImageCollider(Collider):
    pass