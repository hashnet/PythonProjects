from collections import namedtuple
import math

Point2D = namedtuple('Point2D', 'x y')

p1 = Point2D(0, 0)
p2 = Point2D(3, 4)


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


print(dist(p1, p2))