from player import Player
import login
import config
import sys
import mapper
import math
from commands import commands # The dictionary of all commands
#from colorama import init, Fore, Back, Style #For future
#init()


PC = Player()

def setup():
    print(chr(27) + "[2J")
    mapper.loadMap()
    login.createList()
    PC.id, PC.name = login.login()

    PC.loadStats()
    

def prompt():
    userinput = input(str(PC.level_hitpoints[1]) + '/' + str(PC.level_hitpoints[0]) + ' >').lower()
    parseInput(userinput)


def main():
    prompt()


def parseInput(input):
    args = input.split(' ')

    try:
        commands[args[0]].perform(PC, *args)
    except KeyError:
        print('Invalid command: {}'.format(args[0]))

 
##def parseInput(input):
##    arg = input.split(' ')
##
##    if arg[0] == 'kill':
##        print( 'You attack')
##        
##    elif arg[0] in ('n','e','s','w'):
##        location = PC.move(arg[0])
##        mapper.render(location)
##        print( "You move " + arg[0].upper() + " " + str(location) )
##    
##    elif arg[0] == 'attack':
##        PC.gotHit(3)
##
##    elif arg[0] == 'score':
##        PC.showStats()
##
##    elif arg[0] in ('map','m','look','l'):
##        mapper.render(PC.location)
##    
##    else:
##        print( 'Command Unrecognized')

setup()

while True:
    main()

