

########Getting Graphics started#####################
from graphics import *
win = GraphWin('Grid',500,500)

grLnLst = []
for i in range(1,10):
    grLnLst.append(Line(Point(500/10*i,0),Point(500/10*i,499)))
    grLnLst.append(Line(Point(0,500/10*i),Point(499,500/10*i)))

for i in grLnLst:
    i.draw(win)
    
##################################################

########Starting Node Objects#####################

class Node:
    #neighbors to be a {node : distance} dict.
    neighbors = {}
    distance = 99999
    isCurrent = False
    visited = False
    isStart = False
    isEnd = False
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def findDist(otherNode):
        return ((self.x-otherNode.x)**2+(self.y-otherNode.y)**2)**.5

    def addNeighbor(otherNode):
        neighbors[otherNode]= findDist(otherNode)

######################################################

#All objects are to be initialized 'facing' to the right,
#in the (+) x direction.
#Theta rotation is to be counterclockwise.  
class visualObject:
    x = 0
    y = 0
    xSize = 0
    ySize = 0
    thetaDegrees = 0

    def __init__(self,x,y,xSize,ySize,theta):
        self.x = x
        self.y = y
        self.xSize = xSize
        self.ySize = ySize
        self.thetaDegrees = theta

class Ship(visualObject):

    def __init__(self,x,y,xSize,ySize,theta):
        visualObject.__init__(self,x,y,xSize,ySize,theta)

class PlayerShip(Ship):
    def __init__(self,x,y):
        Ship.__init__(self,x,y,50,25,0)
    
    
class Map:
    visObjs = []
    NodeLst = []
    

    
#def main():
    
