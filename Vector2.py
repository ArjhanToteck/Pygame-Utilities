import math
import warnings

class Vector2:

	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y


	def clone(self):
		return Vector2(self.x, self.y)


	def toArray(self):
		return [self.x, self.y]
	
	
	def toTuple(self):
		return (self.x, self.y)
	

	def __str__(self):
		return f"Vector2({self.x}, {self.y})"

	
	def projectOnto(self, other):
        # projection of this vector onto another vector
		dotProduct = self.dot(other)
		lengthSquared = other.x ** 2 + other.y ** 2

		# avoid division by zero
		if lengthSquared != 0:
			projectionScalar = dotProduct / lengthSquared
			projection = Vector2(projectionScalar * other.x, projectionScalar * other.y)

			return projection
		else:
			# if the length squared is zero, return a zero vector
			return Vector2(0, 0)


	def dot(self, other):
        # dot product of two vectors
		return self.x * other.x + self.y * other.y


	def distanceTo(self, other):
		# distance between two vectors
		return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


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