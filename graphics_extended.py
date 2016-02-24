from graphics import *

##class Rotation():
##
##    """2D coordinate rotations"""
##
##    def __init__(self,cx,cy,theta):
##        self.cx = cx
##        self.cy = cy
##        self.mat = [[math.cos(theta),-math.sin(theta),cx],[math.sin(theta),math.cos(theta),cy],[0,0,1]]
##        
##
##    def resX(self,point):
##        return point.x*self.mat[0][0]+point.y*self.mat[0][1] + self.mat[0][2]
##
##    def resY(self,point):
##        return point.x*self.mat[1][0] + point.y*self.mat[1][1] + self.mat[1][2]


win = GraphWin('Grid',500,500)

grLnLst = []
for i in range(1,10):
    grLnLst.append(Line(Point(500/10*i,0),Point(500/10*i,499)))
    grLnLst.append(Line(Point(0,500/10*i),Point(499,500/10*i)))

for i in grLnLst:
    i.draw(win)

trns = Transform(500,500,0,499,499,0)

#print(trns.world(10,10))





tri = Polygon([Point(10,10),Point(10,50),Point(50,10)])
tri.draw(win)
##tri.move(100,0)
tri.rotate(250,250,3.14)
