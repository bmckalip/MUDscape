from player import Player
from npc import NPC
import login
import config
import sys
import mapper
import math
from combat import Combat
from commands import commands # The dictionary of all commands
#from colorama import init, Fore, Back, Style #For future
#init()


PC = Player()
goblin = NPC()
goblin.name = "Goblin"

def setup():
    print(chr(27) + "[2J")
    mapper.loadMap()
    login.createList()
    PC.id, PC.name = login.login()

    PC.loadStats()  

def prompt():
    if PC.inCombat == False: #noncombat prompt hp/hp >
        userinput = input("{}/{} >".format(PC.level_hitpoints[0],PC.level_hitpoints[1])).lower()
    else:
        userinput = input("{}/{} Target: >".format(PC.level_hitpoints[0],PC.level_hitpoints[1])).lower()
        
    parseInput(userinput)


def parseInput(input):
   
    args = input.split(' ')

    if args[0] == 'kill':
        Combat.fight(PC,goblin)

    else: 
        try:
            commands[args[0]].perform(PC, *args)
        except KeyError:
            print('Invalid command: {}'.format(args[0]))
    

def main():
    prompt()





setup()

while True:
    main()

