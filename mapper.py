# -*- coding: utf-8 -*-
import config

def loadMap():
    f = open('mapgrid','r') #load user list
    linelist = []
    
    for line in f:
       linelist.append(line[:-1])
    f.close()

    for i in range(0,len(linelist)):
       linelist[i] = linelist[i].split(',')
       for j in range(0,10):
           config.mapgrid.append(linelist[i][j])

def render(location):
    mapstart = location - 22
    
    print "  -- Room %d --      " % location #room title
    print "╔═══════════════╗"
    for i in range(0,5): #room tiles
        mapline = ""
        for x in range(0,5):
            index = mapstart+x+(10*i)
            mapline += config.mapgrid[index]
            
        print "║               ║"
   
        print "║"+ mapline + "║"
        
    print "╚═══════════════╝"
