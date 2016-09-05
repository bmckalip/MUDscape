import math
from character import Character
from item import Item
from inventory import Inventory

class Player(Character):

    def __init__(self):
        super().__init__(self)
        self.name = ""
        self.level_hitpoints = [10, 10]
        self.level_attack = [1, 1]
        self.level_strength = [1, 1]
        self.level_defense = [1, 1]
        self.level_ranged = [1, 1]
        self.level_prayer = [1, 1]
        self.level_magic = [1, 1]
        self.level_runecrafting = [1, 1]
        self.level_construction = [1, 1]
        self.level_agility = [1, 1]
        self.level_herblore = [1, 1]
        self.level_theiving = [1, 1]
        self.level_crafting = [1, 1]
        self.level_fletching = [1, 1]
        self.level_slayer = [1, 1]
        self.level_hunter = [1, 1]
        self.level_mining = [1, 1]
        self.level_smithing = [1, 1]
        self.level_fishing = [1, 1]
        self.level_cooking = [1, 1]
        self.level_firemaking = [1, 1]
        self.level_woodcutting = [1, 1]
        self.level_farming = [1, 1]

        self.location = 45 #player room ID
        self.level_total = 32
        self.combat = 3
        self.run = 100
        self.flee = False

        self.inventory = Inventory()

    def gainLevel(self, skill):
        skill += 1
        return skill

    def loadStats(self):
        f = open('stats_player', 'r')

        for line in f:
            #parse input line as a list of ints
            attributes = list(map(int, line.split(',')))
            if attributes[0] == self.id:
                self.level_hitpoints = [attributes[1], attributes[2]]
                self.level_attack = [attributes[3], attributes[3]]
                self.level_strength = [attributes[4], attributes[4]]
                self.level_defense = [attributes[5], attributes[5]]
                self.level_ranged = [attributes[6], attributes[6]]
                self.level_prayer = [attributes[7], attributes[7]]
                self.level_magic = [attributes[8], attributes[8]]
                self.level_runecrafting = [attributes[9], attributes[9]]
                self.level_construction = [attributes[10], attributes[10]]
                self.level_agility = [attributes[11], attributes[11]]
                self.level_herblore = [attributes[12], attributes[12]]
                self.level_theiving = [attributes[13], attributes[13]]
                self.level_crafting = [attributes[14], attributes[14]]
                self.level_fletching = [attributes[15], attributes[15]]
                self.level_slayer = [attributes[16], attributes[16]]
                self.level_hunter = [attributes[17], attributes[17]]
                self.level_mining = [attributes[18], attributes[18]]
                self.level_smithing = [attributes[19], attributes[19]]
                self.level_fishing = [attributes[20], attributes[20]]
                self.level_cooking = [attributes[21], attributes[21]]
                self.level_firemaking = [attributes[22], attributes[22]]
                self.level_woodcutting = [attributes[23], attributes[23]]
                self.level_farming = [attributes[24], attributes[24]]
                self.combatLevel()

                attributes = attributes[2:]
                self.level_total = 0
                for attribute in attributes:
                    self.level_total = self.level_total + attribute

    #This is ugly and will need to be changed (obviously) / Just for testing
    def loadInventory(self):
        item1 = Item("Fire rune", 80, True)
        item2 = Item("Water rune", 120, True)
        item3 = Item("Bronze dagger", 1)
        item4 = Item("Iron dagger", 1)
        item5 = Item("Steel dagger", 1)
        item6 = Item("Black dagger", 1)
        item7 = Item("Coins", 1000)
        item8 = Item("Rune scimitar", 1)
        item9 = Item("Steel arrows", 250, True)
        item10 = Item("Lobster", 4)

        self.inventory.addItem(item1)
        self.inventory.addItem(item2)
        self.inventory.addItem(item3)
        self.inventory.addItem(item4)
        self.inventory.addItem(item5)
        self.inventory.addItem(item6)
        self.inventory.addItem(item7)
        self.inventory.addItem(item8)
        self.inventory.addItem(item9)
        self.inventory.addItem(item10)


    def combatLevel(self):
        base = 0.25*(self.level_defense[1] + self.level_hitpoints[1] + math.floor(self.level_prayer[1]/2))
        melee = 0.325*(self.level_attack[1] + self.level_strength[1])
        range = 0.325*(math.floor(self.level_ranged[1]/2) + self.level_ranged[1])
        mage = 0.325*(math.floor(self.level_magic[1]/2) + self.level_magic[1])

        self.combat = math.floor(base + max(melee,range,mage))

    def showStats(self):
        print( "\n*** STATISTICS ***\n")
        print( "{} (level {})\n".format(self.name,self.combat))
        print( "ATT:{}/{}  HIT:{}/{}  MIN:{}/{}".format(self.level_attack[0], self.level_attack[1], self.level_hitpoints[0], self.level_hitpoints[1], self.level_mining[0], self.level_mining[1]))
        print( "STR:{}/{}  AGL:{}/{}  SMT:{}/{}".format(self.level_strength[0], self.level_strength[1], self.level_agility[0], self.level_agility[1], self.level_smithing[0], self.level_smithing[1]))
        print( "DEF:{}/{}  HRB:{}/{}  FSH:{}/{}".format(self.level_defense[0], self.level_defense[1], self.level_herblore[0], self.level_herblore[1], self.level_fishing[0], self.level_fishing[1]))
        print( "RNG:{}/{}  THV:{}/{}  COK:{}/{}".format(self.level_ranged[0], self.level_ranged[1], self.level_theiving[0], self.level_theiving[1], self.level_cooking[0], self.level_cooking[1]))
        print( "PRY:{}/{}  CRF:{}/{}  FIR:{}/{}".format(self.level_prayer[0], self.level_prayer[1], self.level_crafting[0], self.level_crafting[1], self.level_firemaking[0], self.level_firemaking[1]))
        print( "MAG:{}/{}  FLT:{}/{}  WDC:{}/{}".format(self.level_magic[0], self.level_magic[1], self.level_fletching[0], self.level_fletching[1], self.level_woodcutting[0], self.level_woodcutting[1]))
        print( "RNC:{}/{}  SLY:{}/{}  FRM:{}/{}".format(self.level_runecrafting[0], self.level_runecrafting[1], self.level_slayer[0], self.level_slayer[1], self.level_farming[0], self.level_farming[1]))
        print( "CON:{}/{}  HNT:{}/{}  TOT:{}".format(self.level_construction[0], self.level_construction[1], self.level_hunter[0], self.level_hunter[1], self.level_total))
        print( "")

    #This may be unnecessary abstraction, as we can call showInventory from the commands file directly
    def showInventory(self):
        self.inventory.showInventory()


    def move(self, direction):
        if direction == 'n':
            self.location -= 10
        elif direction == 'e':
            self.location += 1
        elif direction == 's':
            self.location += 10
        elif direction == 'w':
            self.location -= 1
        return self.location
