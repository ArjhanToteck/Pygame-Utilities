class Order:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)
    
    def __iter__(self):
        iter(self.items)

    def __next__(self):
        for item in self.items:
            yield item