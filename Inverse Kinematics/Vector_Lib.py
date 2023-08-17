import math

class Vec2():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.theta = 0
        self.get_theta()

    def get_mag(self):
        magnitude = math.sqrt(self.x^2+self.y^2)
        return magnitude

    def add(self, vec):
        return Vec2(self.x+vec.x, self.y+vec.y)

    def subtract(self, vec):
        return Vec2(self.x-vec.x, self.y-vec.y)

    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def get_theta(self):
        if self.x == 0:
            if self.y > 0:
                angle = 90
            else:
                angle = 270
        else:
            angle = math.degrees(math.atan(self.y/self.x))
            if self.x < 0:
                if self.y < 0:
                    angle += 180
                else:
                    angle = 180 + angle

        if angle < 0:
            angle = 360 + angle
        self.theta = angle

    def update(self, x, y):
        self.x = x
        self.y = y
        self.get_theta()