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

        #creates a 5x5 grid of tiles that can be indexed as layout[0][0] (for the first tile, and etc)
        self.tiles = [[Tile() for x in range(5)] for y in range(5)]
        self.drops = []
        self.players = []
        self.NPCs = []
        self.map = ''

        self.__loadRoomTiles()
        self.generateMap()

    def addDrop(self, items, tile):
        if type(items) is ItemStack:
            if type(tile) is Tile and tile in self.tiles:
                tile.addDrop(items) #add drop to tile
                self.__aggregateDrops() #update room drops

    def addOccupant(self, character, tile):
        if type(tile) is Tile and tile in self.tiles:
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
        self.__aggregateDrops()
        self.__aggregateOccupants()
        self.__setEnterable()

    def __aggregateDrops(self):
        if self.tiles:
            for tile in self.tiles:
                for drop in tile.drops:
                    self.drops.append(drop)

    def __aggregateOccupants(self):
        self.__aggregateNPCs()
        self.__aggregatePlayers()

    def __aggregatePlayers(self):
        if self.tiles:
            for tile in self.tiles:
                for member in tile.players:
                    self.players.append(member)

    def __aggregateNPCs(self):
        if self.tiles:
            for tile in self.tiles:
                for member in tile.NPCs:
                    self.NPCs.append(member)

    def __setEnterable(self):
        if self.tiles:
            for tile in self.tiles:
                #if any of room's tiles are enterable, the room is enterable.
                if tile.isEntrance:
                    self.enterable = True
                    break
        #otherwise, room not enterable
        self.enterable = False