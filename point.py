import math

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def dist(self.p):
        d = math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
        return d

point_1 = Point()
point_1.x = 6
point_1.y = 12

point_2 = Point()
point_2.x = 13
point_2.y = 5

print(point_1.dist(point_2))
