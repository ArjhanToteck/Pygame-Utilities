class Color:
    def __init__(self, red = 255, green = 255, blue = 255, alpha = 255):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        
    @classmethod
    def fromHexadecimal(cls):
        # TODO: this
        pass
    
# TODO: make a bunch of static fields for common colors