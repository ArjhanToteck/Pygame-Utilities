from Item import Item

# this is literally just a list wrapper why did we have to do a whole project about this
class Order(list):

	@property
	def items(self):
		return self
	
	def __len__(self):
		return super().__len__()
	
	def __iter__(self):
		return super().__iter__()
	
	def __next__(self):
		return super().__next__()

	def __str__(self):
		result = ""

		for item in self:
			result += item + "\n\n"

	def add(self, __object):
		super().append(__object)

	def calculatePrice(self):
		totalCost = 0

		for item in self.items:
			totalCost += item.calculateTotalPrice()

		return totalCost

	# again, taxes in zelda is crazy, why do we need this function in two places its the same thing?
	def calculateTax(self):
		return self.calculateTax * Item.TAX_PERCENT
			