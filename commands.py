import mapper
import combat
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def perform(self):
        pass


class Kill(Command):
    tokens = ['kill']

    @staticmethod
    def perform(player, *args):

        combat.Combat.fight(player)
        player.inCombat = True


class Stats(Command):
    tokens = ['score','stats']

    @staticmethod
    def perform(player, *args):
        player.showStats()


class Look(Command):
    tokens = ['map', 'm', 'l', 'look']

    @staticmethod
    def perform(player, *args):
        mapper.render(player.location)

class Inventory(Command):
    tokens = ['inv', 'inventory', 'i']

    @staticmethod
    def perform(player, *args):
        player.showInventory()

class Move(Command):
    tokens = ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west']

    @staticmethod
    def perform(player, *args):
        location = player.move(args[0])
        print(location)
        mapper.render(location)
        print('You move {} {}'.format(args[0].upper(), location))

# Create a collection of all tokens and what command they relate to
commands = {}

for cls in Command.__subclasses__():
    for token in cls.tokens:
        commands[token] = cls
