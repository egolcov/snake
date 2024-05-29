import pyxel
from point import Point


class Apple:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def get_cor(self):
        return Point(self.__x, self.__y)

    def draw(self):
        pyxel.pset(self.__x, self.__y, col=8)
