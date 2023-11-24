import pygame

from Vector2 import Vector2

class SpriteSheet:
    def __init__(self, image = None, imagePath = None):
        self.image = image
        self.sprites = {}
        self.sliceData = {}
        
        # load image from path if applicable
        if imagePath != None:
            self.image = pygame.image.load(imagePath)

    class Slice:
        
    	def __init__(self, position, size):
            self.position = position
            self.size = size

    def sliceFromSliceData(self, sliceData = None):
        self.sprites = {}

        if sliceData == None:
            sliceData = self.sliceData
        else:
            self.sliceData = sliceData

        # recursive function for processing
        def processSliceData(data, parentDictionary):
            for key, value in data.items():
                # check if it's another dictionary
                if isinstance(value, dict):
                    # create new parent dictionary for the sprites in this dictionary
                    parentDictionary[key] = {}

                    # recursively process dictionary
                    processSliceData(value, parentDictionary[key])
                else:
                    # cut sprite
                    sprite = self.image.subsurface(pygame.Rect(value.position.x, value.position.y, value.size.x, value.size.y))

                    # add sprite to parent dictionary
                    parentDictionary[key] = sprite

        # start recursion
        processSliceData(sliceData, self.sprites)

        return self.sprites

    def sliceByGrid(self, rows, columns, width, height, rowNames = None, columnNames = None):
        slices = {}

        if rowNames == None:
            rowNames = range(rows)
            
        if columnNames == None:
            columnNames = range(columns)
    
        for y in range(rows):
            rowName = rowNames[y]

            # create row in slices
            slices[rowName] = {}

            for x in range(columns):
                columnName = columnNames[x]

                # get the data needed for slicing sprites and put it in the dictionary
                slice = SpriteSheet.Slice(Vector2(x * width, y * height), Vector2(width, height))
                slices[rowName][columnName] = slice

        # use slice data to slice the sprites
        return self.sliceFromSliceData(slices)

    def sliceByCellSize(self, width, height, rowNames = None, columnNames = None):

        # divide image into a number of rows and columns
        rows = self.image.get_height() / height
        columns = self.image.get_width() / width

        # slice with grid data
        return self.sliceByGrid(rows, columns, width, height, rowNames, columnNames)

    
    def sliceByRowsAndColumns(self, rows, columns, rowNames = None, columnNames = None):
        
        width = self.image.get_width() / columns
        height = self.image.get_height() / rows
        
        # slice with grid data
        return self.sliceByGrid(rows, columns, width, height, rowNames, columnNames)