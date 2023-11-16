import pygame

class SpriteSheet:
    def __init__(self, image = None, imagePath = None):
        self.image = image
        self.sprites = {}
        
        # load image from path if applicable
        if imagePath != None:
            self.image = pygame.image.load(imagePath)


    def sliceByGrid(self, rows, columns, width, height, reset = True)
        if reset:
            self.sprites = {}

            
        # TODO: crop into sprite grid using the width and height of each sprite and number of columns and rows

    def sliceByCellSize(self, width, hight, reset = True):
        
        if reset:
            self.sprites = {}

        # TODO: crop into sprite grid using the width and height of each sprite
        # can just calculate number of columns and rows and call sliceByGrid

        pass

    
    def sliceByRowsAndColumns(self, rows, columns,  reset = True):
        
        if reset:
            self.sprites = {}
            
        # TODO: crop into sprite grid using the number of rows and columns
        # can just calculate cell size and call sliceByGrid

        pass


    def sliceFromDictionary(self, dictionary, reset = True):
        
        if reset:
            self.sprites = {}
        
        # TODO: crop into sprite grid using an inputed dictionary
        # dictionary keys should be name of sprite for easy access and include Vector2 for pixel size and position on image

        pass