class Order:
    def __init__(self):
        self.items = []
        self.currentItem = 0

    def add(self, items):
        if type(items) is list:
            self.items += items
        else:
            self.items.append(items)

    def __len__(self):
        return len(self.items)
    
    def __iter__(self):
        return self

    def __next__(self):
        # check if we need to stop
        if self.currentItem >= len(self.items):
            # reset and close iteration
            self.currentItem = 0
            raise StopIteration
        else:

            # increment current item
            self.currentItem += 1

            # return next item
            return self.items[self.currentItem - 1]
        
