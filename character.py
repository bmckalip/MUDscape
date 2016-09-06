from abc import ABC, abstractmethod
from math import floor

class Character(ABC):

    def __init__(self, charID=-1):
        self.id = charID
        self.name = ''
#       define stats as a list formatted as [currentStat, maxStat]
        self.level_hitpoints = [10, 10]
        self.level_combat = 0

        self.alive = True
        self.invulnerable = False
        self.inCombat = False

#   calculate the characters combat level
  #  @abstractmethod
    def combatLevel(self):
        pass

 #  @abstractmethod
    def loadStats(self):
        pass

#    checks if the character has died
    def __isLethal(self, damage):
        if damage > self.level_hitpoints[0]:
            return True
        return False

    def dealDamage(self, damage):
        if self.invulnerable is True:
            return

        print(self.name + ' Hit for ' + str(damage))
        if self.__isLethal(damage):
            self.alive = False
            print(self.name + ' has been defeated!')

    def takeDamage(self, damage):
        if self.invulnerable is True:
            return
        self.level_hitpoints[0] -= damage
        if self.level_hitpoints[0] <=0:
            self.alive=False

    def hpBar(self):
        healthPercent = self.level_hitpoints[0]/self.level_hitpoints[1]
        if healthPercent >= .8:
            hpbar = '█████'
        elif healthPercent >= .6:
            hpbar = '████░'
        elif healthPercent >= .4:
            hpbar = '███░░'
        elif healthPercent >= .2:
            hpbar = '██░░░'
        elif healthPercent > 0:
            hpbar = '█░░░░'
        elif healthPercent <= 0:
            hpbar = '░░░░░'
        return hpbar
