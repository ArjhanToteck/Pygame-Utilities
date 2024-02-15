import Vector2 as Vector2Cpp

class Vector2:
    def __init__(self, x=0, y=0):
        self.__nativeVector2 = Vector2Cpp.Vector2_new(x, y)


    # getter wrappers

    @property
    def x(self):
        return Vector2Cpp.Vector2_getX(self.__nativeVector2)
    

    @property
    def y(self):
        return Vector2Cpp.Vector2_getY(self.__nativeVector2)

    # setter wrappers

    @x.setter
    def x(self, value):
        Vector2Cpp.Vector2_setX(self.__nativeVector2, value)


    @y.setter
    def y(self, value):
        Vector2Cpp.Vector2_setY(self.__nativeVector2, value)


vector = Vector2(3, 1)
print(vector.x)
vector.x = 123
print(vector.x)
