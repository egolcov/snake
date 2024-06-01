from apple import Apple
from stone import Stone
from point import Point
from snake import Snake
from shovel import Shovel
from puddle import Puddle
from collections import deque
import random
import pyxel


class GameEngine:
    def __init__(self, width: int, height, height_score):
        self.width = width
        self.height = height
        self.height_score = height_score
        self.reset_game()


    def reset_game(self):
        initial_snake = deque([Point(10, 10)])
        self.snakes = [Snake(initial_snake, Point(1, 0), self.width, self.height, self.height_score)]
        self.len_snakes = []
        self.apples = []
        self.stones = []
        self.puddles = []
        self.scores = [1, 1]

        self.apples.append(self.generate_apple())
        self.stones.append(self.generate_stone())

        self.shovels = []
        self.game_over = False

    @staticmethod
    def spawn_probability(probability):
        # probability  [0, 100]
        return probability > random.randint(0, 100)

    def generate_apple(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(self.height_score, self.height - 1)
            apple = Apple(x, y)
            flag = True
            for snake in self.snakes:
                if snake.check_collision(apple.get_cor()):
                    flag = False
            for stone in self.stones:
                a_cor = apple.get_cor()
                s_cor = stone.get_cor()
                if a_cor == s_cor:
                    flag = False
            if flag: return apple

    def generate_stone(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(self.height_score, self.height - 1)
            stone = Stone(x, y)
            flag = True
            for snake in self.snakes:
                if snake.check_collision(stone.get_cor()):
                    flag = False
            for apple in self.apples:
                a_cor = apple.get_cor()
                s_cor = stone.get_cor()
                if a_cor == s_cor:
                    flag = False
            if flag: return stone

    def change_snakes_direction(self, new_direct: Point):
        # если направление хоть какоето
        if new_direct != Point(0, 0):
            # изменяем направление движения всех змеек
            for snake in self.snakes:
                in_puddle = False
                for puddle in self.puddles:
                    if puddle.intersection(snake.get_head()):
                        in_puddle = True
                        break

                if in_puddle:
                    snake.change_direction(new_direct * -1)
                else:
                    snake.change_direction(new_direct)

    def update(self):

        if self.game_over:
            self.snakes = []
            self.apples = []
            self.stones = []
            self.puddles = []
            self.shovels = []

            if pyxel.btnp(pyxel.KEY_R):
                self.reset_game()
            return
        self.scores[1] = sum([snake.get_len() for snake in self.snakes])
        self.scores[0] = max(self.scores)
        new_direct = Point(0, 0)
        # получаем новое направление движения для всех змеек
        if pyxel.btnp(pyxel.KEY_W):
            new_direct = Point(0, -1)
        elif pyxel.btnp(pyxel.KEY_S):
            new_direct = Point(0, 1)
        elif pyxel.btnp(pyxel.KEY_A):
            new_direct = Point(-1, 0)
        elif pyxel.btnp(pyxel.KEY_D):
            new_direct = Point(1, 0)

        self.change_snakes_direction(new_direct)

        # перемещаем всех змеек
        for snake in self.snakes:
            snake.move()

        # убираем змеек у которых произошло самопересечение
        self.snakes = [snake for snake in self.snakes if not snake.check_death()]

        for snake in self.snakes:  # для каждой змейки
            for apple in self.apples:  # пробуем есть яблоки
                if snake.check_collision(apple.get_cor()):
                    snake.eat()
                    self.apples.remove(apple)
                    self.apples.append(self.generate_apple())
                    self.stones.append(self.generate_stone())

        for stone in self.stones:
            # удаляем змеек которые врезались в камень
            self.snakes = [snake for snake in self.snakes if not snake.check_collision(stone.get_cor())]

        # рубим змеек лопатой
        for shovel in self.shovels:
            if not shovel.is_alive():  # если лопата рубит
                self.new_snakes = []
                for snake in self.snakes:
                    self.new_snakes += snake.separate(shovel.get_cors())
                self.snakes = self.new_snakes

        # удаляем не используемые лопаты
        self.shovels = [shovel for shovel in self.shovels if shovel.is_alive()]

        # удаляем пересохшие лужи
        self.puddles = [puddle for puddle in self.puddles if puddle.is_alive()]

        if self.spawn_probability(1):
            self.shovels.append(Shovel(self.width, self.height, self.height_score))

        if self.spawn_probability(1):
            self.puddles.append(Puddle(self.width, self.height, self.height_score))

        # если больше не осталось змеек
        if not self.snakes:
            self.game_over = True

    def draw(self):
        pyxel.cls(4)
        # рисуем лужи
        for puddle in self.puddles:
            puddle.draw()

        for snake in self.snakes:
            snake.draw()

        for apple in self.apples:
            apple.draw()

        for stone in self.stones:
            stone.draw()

        for shovel in self.shovels:
            shovel.draw()

        pyxel.rect(0, 0, self.width, self.height_score, 14)

        pyxel.text(2, 2, f'{sum([snake.get_len() for snake in self.snakes]):04}', 4)
        if self.game_over:
            pyxel.text(self.width // 2 - 20, self.height // 2 - 13,
                       f"  MAX: {self.scores[0]}\n TOTAL: {self.scores[1]}\n\nGAME OVER!\n PRESS 'R' \nTO RESTART", 14)

    def run(self):
        pyxel.init(self.width, self.height, fps=17)
        pyxel.run(self.update, self.draw)

