from Item.Item import Item

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
		result = f"Total: {self.calculatePrice()}\nTax: {self.calculateTax()}\n"

		for item in self:
			result += item.toString() + "\n\n"

		return result


	def toString(self):
		return self.__str__()


	def add(self, __object):
		super().append(__object)


	def addItem(self, item):
		for stack in self:
			if stack.name == item.name:
				stack.quantity += 1
				return
			
		self.add(item)

	def calculatePrice(self):
		totalCost = 0

		for item in self.items:
			totalCost += item.calculateTotalPrice()

		return totalCost

	# again, taxes in zelda is crazy, why do we need this function in two places its the same thing?
	def calculateTax(self):
		return self.calculatePrice() * Item.TAX_PERCENT
			