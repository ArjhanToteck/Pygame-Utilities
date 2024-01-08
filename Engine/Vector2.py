import math
import warnings

from Engine import *
from ctypes import Structure, c_float

# wrapper for c++ Vector2
class Vector2(Structure):
	_fields_ = [("x", c_float), ("y", c_float)]

	@staticmethod
	def distance(v1, v2):
		# distance between two vectors
		return math.sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)	
	
	def __init__(self, x = 0, y = 0):
		self.pointer = cppEngine.Vector2_init(x, y)
		print(self.x)

	# properties
	@property
	def x(self):
		test = cppEngine.Vector2_getX(self.pointer)
		print(test)
		return test
	
	@x.setter
	def setX(self, value):
		return cppEngine.Vector2_setX(self.pointer, value)

	@property
	def y(self):
		return cppEngine.Vector2_getY(self.pointer)
	
	@y.setter
	def setY(self, value):
		return cppEngine.Vector2_setY(self.pointer, value)

	# nonstatic methods

	def clone(self):
		return Vector2(self.x, self.y)


	def toArray(self):
		return [self.x, self.y]
	
	
	def toTuple(self):
		return (self.x, self.y)
	

	# operator overloads

	def __str__(self):
		return f"Vector2({self.x}, {self.y})"


	def __eq__(self, other):
		# check if multiplied by another Vector2
		if isinstance(other, Vector2):
			return self.x == other.x and self.y == other.y


	def __mul__(self, other):
		# check if multiplied by another Vector2
		if isinstance(other, Vector2):
			return Vector2(self.x * other.x, self.y * other.y)
		# check if multiplied by number
		elif isinstance(other, int) or isinstance(other, float):
			return Vector2(self.x * other, self.y * other)
		else:
			warnings.warn("This operation is not implemented.")


	def __rmul__(self, other):
		return self * other


	def __add__(self, other):
		# check if added to another Vector2
		if isinstance(other, Vector2):
			return Vector2(self.x + other.x, self.y + other.y)
		# check if added to number
		elif isinstance(other, int) or isinstance(other, float):
			return Vector2(self.x + other, self.y + other)
		else:
			warnings.warn("This operation is not implemented.")
				

	def __sub__(self, other):
		# check if subtracted from another Vector2
		if isinstance(other, Vector2):
			return Vector2(self.x - other.x, self.y - other.y)
		# check if subtracted by number
		elif isinstance(other, int) or isinstance(other, float):
			return Vector2(self.x - other, self.y - other)
		else:
			warnings.warn("This operation is not implemented.")
	

	def __truediv__(self, other):
		# check if divided by another Vector2
		if isinstance(other, Vector2):
			return Vector2(self.x / other.x, self.y / other.y)
		# check if divided by number
		elif isinstance(other, int) or isinstance(other, float):
			return Vector2(self.x / other, self.y / other)
		else:
			warnings.warn("This operation is not implemented.")
	

	def __pow__(self, other):
		# check if multiplied by another Vector2
		if isinstance(other, Vector2):
			return Vector2(self.x ** other.x, self.y ** other.y)
		# check if multiplied by number
		elif isinstance(other, int) or isinstance(other, float):
			return Vector2(self.x ** other, self.y ** other)
		else:
			warnings.warn("This operation is not implemented.")

	def __abs__(self):
		return Vector2(abs(self.x), abs(self.y))

	def __neg__(self):
		return Vector2(-self.x, -self.y)
	
cppEngine.Vector2_init.restype = ctypes.POINTER(Vector2)

# static properties (reference itself)
Vector2.zero = Vector2(0, 0)
Vector2.one = Vector2(1, 1)

Vector2.up = Vector2(0, 1)
Vector2.down = Vector2(0, -1)
Vector2.right = Vector2(1, 0)
Vector2.left = Vector2(-1, 0)