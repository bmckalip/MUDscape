from tile import Tile
from itemStack import ItemStack

class Room:

    def __init__(self, roomID):
        self.id = roomID
        self.enterable = True

        #creates a 5x5 grid of tiles that can be indexed as layout[0][0] (for the first tile, and etc)
        self.layout = [[Tile() for x in range(5)] for y in range(5)]
        self.droppedItems = []
        self.players = []
        self.NPCs = []

        self.__loadRoomTemplate()

    def addDroppedItem(self, items, location):
        if type(items) is ItemStack:
            self.droppedItems.append(items)

    def getDroppedItems(self):
        pass

    def __loadRoomTemplate(self):
        try:
            open('rooms/tiles/' + self.id, 'r')
            #TODO parse room file
        except IOError:
            print('Room does not exist')
