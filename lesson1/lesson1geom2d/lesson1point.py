from math import sqrt


class Point:
    def __init__(self, x, y):  # конструктор, self - объект, x, y - значения
        self.x = x  # значение x присваивается атрибуту x объекта Point (атрибут может называться как переменная)
        self.y = y

    def distance(self, p2):  # метод класса
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx ** 2 + dy ** 2)

    def __eq__(self, other):    # сравнение двух точек
        return self.x == other.x and self.y == other.y