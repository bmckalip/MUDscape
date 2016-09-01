import math
from character import Character


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

    def gainLevel(self, skill):
        skill += 1
        return skill

    def loadStats(self):
        f = open('stats_player', 'r')
        
        for line in f:
            #parse input line as a list of ints
            attributes = list(map(int, line.split(',')))
            if line[0] == self.id:
                self.level_hitpoints = [attributes[1], attributes[2]]
                self.level_attack = attributes[3]
                self.level_strength = attributes[4]
                self.level_defense = attributes[5]
                self.level_ranged = attributes[6]
                self.level_prayer = attributes[7]
                self.level_magic = attributes[8]
                self.level_runecrafting = attributes[9]
                self.level_construction = attributes[10]
                self.level_agility = attributes[11]
                self.level_herblore = attributes[12]
                self.level_theiving = attributes[13]
                self.level_crafting = attributes[14]
                self.level_fletching = attributes[15]
                self.level_slayer = attributes[16]
                self.level_hunter = attributes[17]
                self.level_mining = attributes[18]
                self.level_smithing = attributes[19]
                self.level_fishing = attributes[20]
                self.level_cooking = attributes[21]
                self.level_firemaking = attributes[22]
                self.level_woodcutting = attributes[23]
                self.level_farming = attributes[24]
                self.combatLevel()

            attributes = attributes[2:]
            self.level_total = 0
            for attribute in attributes:
                self.level_total = self.level_total + attribute
            
    def combatLevel(self):
        base = 0.25*(self.defense + self.hitpoints + math.floor(self.prayer/2))
        melee = 0.325*(self.attack + self.strength)
        range = 0.325*(math.floor(self.ranged/2) + self.ranged)
        mage = 0.325*(math.floor(self.magic/2) + self.magic)

        self.combat = math.floor(base + max(melee,range,mage))
    
    def showStats(self):
        print( "")
        print( "*** STATISTICS ***")
        print( "")
        print( "{} (level {})".format(self.name,self.combat))
        print( "")
        print( "ATT:{}/{}  HIT:{}/{}  MIN:{}/{}".format(self.level_attack[0], self.level_attack[1], self.level_hitpoints[0], self.level_hitpoints[1], self.level_mining[0], self.level_mining[1]))
        print( "STR:{}/{}  AGL:{}/{}  SMT:{}/{}".format(self.level_strength[0], self.level_strength[1], self.level_agility[0], self.level_agility[1], self.level_smithing[0], self.level_smithing[1]))
        print( "DEF:{}/{}  HRB:{}/{}  FSH:{}/{}".format(self.level_defense[0], self.level_defense[1], self.level_herblore[0], self.level_herblore[1], self.level_fishing[0], self.level_fishing[1]))
        print( "RNG:{}/{}  THV:{}/{}  COK:{}/{}".format(self.level_ranged[0], self.level_ranged[1], self.level_theiving[0], self.level_theiving[1], self.level_cooking[0], self.level_cooking[1]))
        print( "PRY:{}/{}  CRF:{}/{}  FIR:{}/{}".format(self.level_prayer[0], self.level_prayer[1], self.level_crafting[0], self.level_crafting[1], self.level_firemaking[0], self.level_firemaking[1]))
        print( "MAG:{}/{}  FLT:{}/{}  WDC:{}/{}".format(self.level_magic[0], self.level_magic[1], self.level_fletching[0], self.level_fletching[1], self.level_woodcutting[0], self.level_woodcutting[1]))
        print( "RNC:{}/{}  SLY:{}/{}  FRM:{}/{}".format(self.level_runecrafting[0], self.level_runecrafting[1], self.level_slayer[0], self.level_slayer[1], self.level_farming[0], self.level_farming[1]))
        print( "CON:{}/{}  HNT:{}/{}  TOT:{}".format(self.level_construction[0], self.level_construction[1], self.level_hunter[0], self.level_hunter[1], self.level_total))
        print( "")

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
