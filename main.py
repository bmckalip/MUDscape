import player
import login
import config
import sys
import mapper
import math
#import command

from colorama import init, Fore, Back, Style #For future 
init()


PC = player.player()

def setup():
    mapper.loadMap()
    login.createList()
    PC.id,PC.name = login.login()

    if PC.id == 1:
        PC.loadStats()
    

def prompt():
    userinput = input(str(PC.hitpoints) +'/'+ str(PC.currentHitpoints) + ' >').lower()
    parseInput(userinput)

def main():
    prompt()
 
def parseInput(input):
    arg = input.split(' ')

    if arg[0] == 'kill':
        print( 'You attack')
        
    elif arg[0] in ('n','e','s','w'):
        location = PC.move(arg[0])
        mapper.render(location)
        print( "You move " + arg[0].upper() + " " + str(location) )
    
    elif arg[0] == 'attack':
        PC.gotHit(3)

    elif arg[0] == 'score':
        PC.showStats()

    elif arg[0] in ('map','m','look','l'):
        mapper.render(PC.location)
    
    else:
        print( 'Command Unrecognized')

  #Commands = {
  # 'quit': PC.quit,
  # 'attack': PC.gotHit,
  # }   
  #  if len(args) > 0:
  #      commandFound = False
  #      for c in Commands.keys():
  #          if args[0] == c[:len(args[0])]:
  #              Commands[c](3)
  #              commandFound = True
  #              break
  #      if not commandFound:
  #          print( "Invalid Command")
            
#--------------------------------------------------
setup()

while True:
    main()

