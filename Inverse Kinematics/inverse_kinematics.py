from math import acos, atan, cos, sin, dist, radians
import Vector_Lib as Vec

class segment():
    def __init__(self, a, angle, length):
        self.a = a
        self.length = length
        self.angle = angle
        self.b = Vec.Vec2(0,0)
        self.calculateB()

    def calculateB(self):
        bx = self.length*cos(radians(self.angle))
        by = self.length*sin(radians(self.angle))

        self.b.update(self.a.x + bx, self.a.y + by)


    def calculateA(self):
        dx = self.length*cos(radians(self.angle))
        dy = self.length*sin(radians(self.angle))

        self.a.update(self.b.x - dx, self.b.y - dy)


    def setA(self, pos):
        self.a.update(pos.x, pos.y)
        self.calculateB()


    def follow(self, target):

        pointer = Vec.Vec2(target.x-self.a.x, target.y - self.a.y)
        self.angle = pointer.theta

        self.b = target
        self.calculateA()