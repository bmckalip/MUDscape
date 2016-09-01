class enemy:

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
        self.combat = 1

    def combatLevel(self):
        base = 0.25*(self.defense + self.hitpoints + math.floor(self.prayer/2))
        melee = 0.325*(self.attack + self.strength)
        range = 0.325*(math.floor(self.ranged/2) + self.ranged)
        mage = 0.325*(math.floor(self.magic/2) + self.magic)

        self.combat = math.floor(base + max(melee,range,mage))        

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

        self.combatLevel()

    def gotHit(self, damage):
        print 'Hit for ' + str(damage)


    
