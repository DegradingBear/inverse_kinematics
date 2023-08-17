import Vector_Lib as vec
import inverse_kinematics as segment

class tentacle():
    def __init__(self, base, num_segments, length):
        self.base = base
        self.segments = [segment.segment(vec.Vec2(0,0), 90, length) for i in range(num_segments)]


    def update(self, target):
        self.segments[-1].follow(vec.Vec2(target.x,target.y))

        length = len(self.segments)
        i = length-2
        while i >= 0:
            self.segments[i].follow(self.segments[i+1].a)
            i -= 1

        self.segments[0].setA(self.base)
        i = 1
        while i < length:
            self.segments[i].setA(self.segments[i-1].b)
            i += 1

