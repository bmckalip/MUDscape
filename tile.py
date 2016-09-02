from itemStack import ItemStack
from npc import NPC
from player import Player

class Tile:

    def __init__(self):
        self.droppedItems = [];
        self.type = 'terrain'
        self.icon = ' . '
        self.traversable = True
        self.NPCs = []
        self.players = []

    def addDroppedItem(self, item):
        for entry in self.droppedItems:
            if(entry.itemID == item.itemID):
                entry.combine(item)
                return
        self.droppedItems.append(item)

    def removeDroppedItem(self, item):
        if type(item) is ItemStack and item in self.droppedItems:
            self.droppedItems.remove(item)

    def addOccupant(self, character):
        if not self.traversable:
            return False
        if type(character) is NPC:
            self.NPCs.append(character)
        elif type(character) is Player:
            self.players.append(character)

    def removeOccupant(self, character):
        #the remove function only removes an object if it exists, an additional check is not required
        if type(character) is NPC:
            self.NPCs.remove(character)
        elif type(character) is Player:
            self.players.remove(character)