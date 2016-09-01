from character import Character
import math


class NPC(Character):

    def __init__(self):
        super().__init__(self)
        self.name = ""
        self.aggressive = False

        self.level_hitpoints = [1, 1]
        self.level_attack = [0, 0]
        self.level_strength = [0, 0]
        self.level_defense = [0, 0]
        self.level_ranged = [0, 0]
        self.level_magic = [0, 0]
        self.level_prayer = [0, 0]

        self.loadStats()
        self.combatLevel()

    def loadStats(self):
        f = open('stats_npc', 'r')
        for line in f:
            attribute = int(line.split(','))
            if line[0] == self.id:
                self.level_hitpoints = [attribute[1], attribute[2]]
                self.level_attack = [attribute[3], attribute[3]]
                self.level_strength = [attribute[4], attribute[4]]
                self.level_defense = [attribute[5], attribute[5]]
                self.level_ranged = [attribute[6], attribute[6]]
                self.level_prayer = [attribute[7], attribute[7]]
                self.level_magic = [attribute[8], attribute[8]]
        self.combatLevel()

    def combatLevel(self):
        base = 0.25*(self.level_defense[1] + self.level_hitpoints[1] + math.floor(self.level_prayer[1]/2))
        melee = 0.325*(self.level_attack[1] + self.level_strength[1])
        range = 0.325*(math.floor(self.level_ranged[1]/2) + self.level_ranged[1])
        mage = 0.325*(math.floor(self.level_magic[1]/2) + self.level_magic[1])

        self.level_combat = math.floor(base + max(melee, range, mage))

