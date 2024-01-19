# this is literally just a list with different property names why did we have to do a whole project surrounding this
class Order(list):
    def add(self, __object):
        return super().append(__object)

    def __len__(self):
        return super().__len__()
    
    def __iter__(self):
        return super().__iter__()
    
    def __next__(self):
        return super().__next__()

    @property
    def items(self):
        return self