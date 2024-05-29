import pyxel
import time
from point import Point
from random import randint, choice


class Shovel:
    shovel_size = 15  # количество пикселей для лопаты

    def __init__(self, width, height, height_score):
        self.direction = choice(["vertical", "horizontal"])
        self.start_time = time.time()
        self.shovel = []
        self.alive = True  # нужно ли ее рисовать и поддерживать
        if (self.direction == "vertical"):
            p = Point(randint(0, width), randint(height_score, height - self.shovel_size))
        else:  # горризонтальная
            p = Point(randint(0, width - self.shovel_size), randint(height_score, height))
        self.shovel.append(p)  # заносим первый элемент в список пикселей
        for i in range(self.shovel_size):
            if self.direction == "vertical":
                self.shovel.append(Point(
                    self.shovel[-1].x(),
                    self.shovel[-1].y() + 1
                ))
            else:  # горризонтальная
                self.shovel.append(Point(
                    self.shovel[-1].x() + 1,
                    self.shovel[-1].y()
                ))

    def is_alive(self):  # возращает нужно ли рисовать лопату в дальнейшем
        return self.alive

    def get_cors(self):  # возращает пиксели на экране которые подпадают под лопату
        return self.shovel

    def draw(self):
        for i, point in enumerate(self.shovel):
            if time.time() - self.start_time < 2:
                colour = 13
            else:
                colour = 9
                self.alive = False
            pyxel.pset(point.x(), point.y(), col=colour)  # рисуем пиксель лопаты на экран
