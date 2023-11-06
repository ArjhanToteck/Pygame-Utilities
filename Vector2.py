import warnings

class Vector2:

	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y


	def toArray(self):
		return [self.x, self.y]
	
	
	def toTuple(self):
		return (self.x, self.y)


	def __eq__(self, other):
		# check if multiplied by another Vector2
		if isinstance(other, Vector2):
			return self.x == other.x and self.y == other.x


	def __mul__(self, other):
		# check if multiplied by another Vector2
		if isinstance(other, Vector2):
			return Vector2(self.x * other.x, self.y * other.y)
		# check if multiplied by number
		elif isinstance(other, int) or isinstance(other, float):
			return Vector2(self.x * other, self.y * other)
		else:
			warnings.warn("This operation is not implemented.")


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

	def __str__(self):
		return f"Vector2({self.x}, {self.y})"