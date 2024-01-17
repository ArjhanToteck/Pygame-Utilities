class Order(list):
    def add(self, items):
        if type(items) is list:
            self += items
        else:
            self.append(items)

    @property
    def items(self):
        return self
    
    def __len__(self):
        super().__len__(self)
    

    def __iter__(self):
        super().__iter__(self)

    def __next__(self):
        super().__next__(self)
