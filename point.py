class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.__x == other.__x and self.__y == other.__y

    def __ne__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.__x != other.__x or self.__y != other.__y

    def __hash__(self):
        return hash((self.__x, self.__y))

    def __assign__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        self.__x = other.__x
        self.__y = other.__y
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # Умножение вектора на скаляр
            return Point(self.__x * other, self.__y * other)
