#TODO
#finish loadRoomTiles() function
#finish generateMap() function

from tile import Tile
from itemStack import ItemStack
from character import Character
from npc import NPC
from player import Player

class Room:

    def __init__(self, roomID):
        self.id = roomID
        self.enterable = False

        #creates a grid of tiles that can be indexed as tiles[0][0] (for the first tile, and etc)
        self.roomSize = 100
        self.tiles = [[Tile() for x in range(self.roomSize)] for y in range(self.roomSize)]
        self.drops = []
        self.players = []
        self.NPCs = []
        self.map = ''

        self.__loadRoomTiles()
        self.generateMap()

    def addDrop(self, items, tile):
        if type(items) is ItemStack:
            if type(tile) is Tile:
                tile.addDrop(items) #add drop to tile
                self.__aggregateDrops() #update room drops

    def addOccupant(self, character, tile):
        if type(tile) is Tile:
            tile.addOccupant(character)
            self.__aggregateOccupants()

    def generateMap(self):
        for tile in self.tiles:
            pass

    def __loadRoomTiles(self):
        try:
            open('rooms/tiles/' + self.id, 'r')
            #TODO parse room file
            self.__aggregateTileInfo()
        except IOError:
            print('Room does not exist')

    def __aggregateTileInfo(self):
        if self.tiles:
            for i in range(self.roomSize):
                for j in range(self.roomSize):
                    tile = self.tiles[i][j]
                    self.__aggregateDrops(tile)
                    self.__aggregateNPCs(tile)
                    self.__aggregatePlayers(tile)
                    self.__setEnterable(tile)

    def __aggregateDrops(self, tile):
        for drop in tile.drops:
            if drop not in self.drops:
                self.drops.append(drop)

    def __aggregatePlayers(self, tile):
        for member in tile.players:
            if member not in self.players:
                self.players.append(member)

    def __aggregateNPCs(self, tile):
        for member in tile.NPCs:
            if member not in self.NPCs:
                self.NPCs.append(member)

    def __setEnterable(self, tile):
        #if any of room's tiles are enterable, the room is enterable.
        if tile.isEntrance:
            self.enterable = True
        #otherwise, room not enterable
        self.enterable = False