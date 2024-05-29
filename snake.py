import pyxel
from collections import deque
from point import Point


class Snake:
    '''
    принимает:
      snake - deque с начальной змейкой
      direction - Point с направлением змейки
      width_board - ширина экрана
      height_board - высота экрана
      height_score - высота счетчика1

    '''

    def __init__(self, snake, direction: Point, width_board, height_board, height_score):
        self.snake = snake
        self.direction = direction
        self.width_board = width_board
        self.height_board = height_board
        self.height_score = height_score

    def change_direction(self, new_direction: Point):
        # Проверяем, что новое направление не является обратным текущему направлению
        if (new_direction.x() != -self.direction.x()) or (new_direction.y() != -self.direction.y()):
            self.direction = new_direction

    def get_direction(self):
        return self.direction

    def get_head(self):
        return self.snake[0]

    def move(self):  # перемещяет змейку в направлении
        self.__new_head()  # добавляем голову
        self.snake.pop()  # удаляем хвост

    def check_death(self):
        """ проверяет самоперессечение змейки. Возращает наличие самопересечения"""
        if len(self.snake) != len(set(self.snake)):
            return True
        return False

    def check_collision(self, p: Point):  # проверяет столкновение с пикселем Point на экране
        for i in self.snake:
            if p == i:
                return True
        return False

    def separate(self, shovel):
        parts = [deque()]
        for snake_p in self.snake:
            flag = True
            for shovel_p in shovel:
                if snake_p == shovel_p:
                    parts.append(deque())
                    flag = False
                    break
            if flag:
                parts[-1].append(snake_p)

        snakes = []
        for part in parts:
            if part:
                snakes.append(Snake(part, self.direction, self.width_board, self.height_board, self.height_score))
        return snakes

    def eat(self):
        self.__new_head()

    def __new_head(self):
        old_head = self.snake[0]
        # считаем координаты новой головы с учетом (не/да) перевернутого направления
        new_head = Point(
            (old_head.x() + self.direction.x()) % self.width_board,
            (old_head.y() + self.direction.y() - self.height_score) % (
                    self.height_board - self.height_score) + self.height_score
        )
        self.snake.appendleft(new_head)  # ставим новую голову

    def get_len(self):
        return len(self.snake)

    def draw(self):  # рисуем змейку
        for i, point in enumerate(self.snake):
            if i == 0:  # голова
                colour = 7
            else:  # тело
                colour = 15
            pyxel.pset(point.x(), point.y(), col=colour)  # рисуем пиксель змейки на экран
