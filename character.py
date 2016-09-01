from abc import ABC, abstractmethod
import math


class Character(ABC):

    def __init__(self, charID=-1):
        self.id = charID
        self.name = ''
#       define stats as a list formatted as [currentStat, maxStat]
        self.level_hitpoints = [10, 10]
        self.level_combat = 0

        self.alive = True
        self.invulnerable = False

#   calculate the characters combat level
    @abstractmethod
    def combatLevel(self):
        pass

    @abstractmethod
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