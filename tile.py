#TODO
#define available terrain types and associate icons with them
#expand entrances to allow for multiple levels

from itemStack import ItemStack
from npc import NPC
from player import Player

class Tile:

    def __init__(self):
        self.drops = [];
        self.type = 'terrain'
        self.icon = ' . '
        self.traversable = True
        self.isEntrance = False
        self.NPCs = []
        self.players = []

    def addDrop(self, item):
        for entry in self.drops:
            if(entry.itemID == item.itemID):
                entry.combine(item)
                return
        self.drops.append(item)

    def removeDrop(self, item):
        if type(item) is ItemStack:
            self.drops.remove(item)

    def addOccupant(self, character):
        if not self.traversable:
            return False
        if type(character) is NPC:
            self.NPCs.append(character)
        elif type(character) is Player:
            self.players.append(character)
        else:
            return False

    def removeOccupant(self, character):
        #the remove function only removes an object if it exists, an additional check is not required
        if type(character) is NPC:
            self.NPCs.remove(character)
        elif type(character) is Player:
            self.players.remove(character)
