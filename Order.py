class Order(list):
    def add(self, __object):
        return super().append(__object)

    def __len__(self):
        return super().__len__()
    
    def __iter__(self):
        return super().__iter__()

    @property
    def items(self):
        return self