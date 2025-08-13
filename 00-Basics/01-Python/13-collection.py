from collections import Counter

string: str = "aabbcccdddddd"
count = Counter(string)
for key, value in count.items():
    print(f"{key} -> {value}")
# a -> 2
# b -> 2
# c -> 3
# d -> 6

print(count.most_common(2))
# [('d', 6), ('c', 3)]

###################################################################################

from collections import namedtuple
Point = namedtuple("Point", "x,y")


def addPoint(a: Point, b: Point):
    return Point(a.x + b.x, a.y + b.y)


pt1: Point = Point(2, -3)
pt2: Point = Point(0, 9)
resultPoint = addPoint(pt1, pt2)
print(resultPoint)
# Point(x=2, y=6)

###################################################################################

from collections import OrderedDict
ord_dict = OrderedDict()
ord_dict['v'] = 1
ord_dict['n'] = 4
ord_dict['a'] = 2
print(ord_dict)
# OrderedDict([('v', 1), ('n', 4), ('a', 2)])
