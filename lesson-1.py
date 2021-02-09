from math import sqrt

'''from lesson1geom2d.lesson1point import Point'''

from lesson1geom2d import *  # импорт в соответствии с файлом init

a = Point(0, 0)
b = Point(3, 4)

print(a.distance(
    b))  # Point(0, 0) - объект, в котором функция вызывается, Point(3, 4) - объект, в котором передается этот метод
print(a == b)
print(a == Point(0, 0))

'Функция с аргументами - объектами типа Point'


def distance(p1, p2):  # аргументы - два объекта типа Point
    dx = p2.x - p1.x  # название_объекта.название атрибута
    dy = p2.y - p1.y
    return sqrt(dx ** 2 + dy ** 2)


print(distance(a, b))
