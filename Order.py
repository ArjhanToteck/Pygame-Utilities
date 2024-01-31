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

    def add(self, __object):
        super().append(__object)

    def calculatePrice(self):
        totalCost = 0

        for item in self.items:
            totalCost += item.calculateTotalPrice()

        return totalCost

    def calculateTax(self, taxPercent = 0.0725):
        return self.calculateTax * taxPercent
            