import pyxel
import time
from random import randint
from point import Point


class Puddle:
    puddle_radius = [0, 2, 4, 6, 8, 10, 10, 10, 8, 6, 4, 2, 0]

    def __init__(self, width, height, height_score):
        self.start_time = time.time()
        self.puddle = []
        self.alive = True
        self.p = Point(randint(max(self.puddle_radius), width - max(self.puddle_radius)),
                       randint(height_score + max(self.puddle_radius), height - max(self.puddle_radius)))
        self.cur_index_radius = 0
        self.change_duration = 2  # Duration in seconds for each radius change
        self.build_puddle()

    def is_alive(self):
        return self.alive

    def intersection(self, p: Point) -> bool:
        for i in self.puddle:
            if p == i:
                return True
        return False

    def draw(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        # Update radius index based on elapsed time
        if elapsed_time >= self.change_duration:
            self.cur_index_radius += 1
            self.start_time = current_time

            if self.cur_index_radius >= len(self.puddle_radius):
                self.alive = False
                return

            self.build_puddle()

        colour = 6
        for point in self.puddle:
            pyxel.pset(point.x(), point.y(), col=colour)

    def build_puddle(self):
        self.puddle = []
        radius = self.puddle_radius[self.cur_index_radius]
        for x in range(self.p.x() - radius, self.p.x() + radius + 1):
            for y in range(self.p.y() - radius, self.p.y() + radius + 1):
                if (self.p.x() - x) ** 2 + (self.p.y() - y) ** 2 <= radius ** 2:
                    self.puddle.append(Point(x, y))
