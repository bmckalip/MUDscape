import math

class player:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.hitpoints = 10
        self.currentHitpoints = 10
        self.attack = 1
        self.strength = 1
        self.defense = 1
        self.ranged = 1
        self.prayer = 1
        self.magic = 1
        self.runecrafting = 1
        self.construction = 1
        self.agility = 1
        self.herblore = 1
        self.theiving = 1
        self.crafting = 1
        self.fletching = 1
        self.slayer = 1
        self.hunter = 1
        self.mining = 1
        self.smithing = 1
        self.fishing = 1
        self.cooking = 1
        self.firemaking = 1
        self.woodcutting = 1
        self.farming = 1
        self.location = 45 #player room ID
        self.total = 32
        self.combat = 3
        self.run = 100

    def gainLevel(self, skill):
        skill = skill + 1
        return skill

    def loadStats(self):
        f = open('statlist','r')
        for line in f:
            if line[:1] == str(self.id):
                stat = line.split(',')
                self.hitpoints = int(stat[1])
                self.currentHitpoints = int(stat[2])
                self.attack = int(stat[3])
                self.strength = int(stat[4])
                self.defense = int(stat[5])
                self.ranged = int(stat[6])
                self.prayer = int(stat[7])
                self.magic = int(stat[8])
                self.runecrafting = int(stat[9])
                self.construction = int(stat[10])
                self.agility = int(stat[11])
                self.herblore = int(stat[12])
                self.theiving = int(stat[13])
                self.crafting = int(stat[14])
                self.fletching = int(stat[15])
                self.slayer = int(stat[16])
                self.hunter = int(stat[17])
                self.mining = int(stat[18])
                self.smithing = int(stat[19])
                self.fishing = int(stat[20])
                self.cooking = int(stat[21])
                self.firemaking = int(stat[22])
                self.woodcutting = int(stat[23])
                self.farming = int(stat[24])
                
        self.combatLevel()

        for i in range(1,24):
            self.total = self.total + int(stat[i])         
            
    def combatLevel(self):
        base = 0.25*(self.defense + self.hitpoints + math.floor(self.prayer/2))
        melee = 0.325*(self.attack + self.strength)
        range = 0.325*(math.floor(self.ranged/2) + self.ranged)
        mage = 0.325*(math.floor(self.magic/2) + self.magic)

        self.combat = math.floor(base + max(melee,range,mage))
    
    def showStats(self):
        print ""
        print "*** STATISTICS ***"
        print ""
        print "%s (level %d)" % (self.name,self.combat)
        print ""
        print "ATT:%d/%d  HIT:%d/%d  MIN:%d/%d" % (self.attack, self.attack, self.currentHitpoints, self.hitpoints, self.mining, self.mining)
        print "STR:%d/%d  AGL:%d/%d  SMT:%d/%d" % (self.strength, self.strength, self.agility, self.agility, self.smithing, self.smithing)
        print "DEF:%d/%d  HRB:%d/%d  FSH:%d/%d" % (self.defense, self.defense, self.herblore, self.herblore, self.fishing, self.fishing)
        print "RNG:%d/%d  THV:%d/%d  COK:%d/%d" % (self.ranged, self.ranged, self.theiving, self.theiving, self.cooking, self.cooking)
        print "PRY:%d/%d  CRF:%d/%d  FIR:%d/%d" % (self.prayer, self.prayer, self.crafting, self.crafting, self.firemaking, self.firemaking)
        print "MAG:%d/%d  FLT:%d/%d  WDC:%d/%d" % (self.magic, self.magic, self.fletching, self.fletching, self.woodcutting, self.woodcutting)
        print "RNC:%d/%d  SLY:%d/%d  FRM:%d/%d" % (self.runecrafting, self.runecrafting, self.slayer, self.slayer, self.farming, self.farming)
        print "CON:%d/%d  HNT:%d/%d  TOT:%d" % (self.construction, self.construction, self.hunter, self.hunter, self.total)
        print ""

    def gotHit(self, damage):
        print 'Hit for ' + str(damage)

    def move(self, direction):
        if direction == 'n':
            self.location = self.location - 10
        elif direction == 'e':
            self.location = self.location + 1
        elif direction == 's':
            self.location = self.location + 10
        elif direction == 'w':
            self.location = self.location - 1
        return self.location
            
        
