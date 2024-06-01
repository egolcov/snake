import unittest
from collections import deque
from point import Point
from snake import Snake
from puddle import Puddle
from game_engine import GameEngine

class TestSnake(unittest.TestCase):
    def setUp(self):
        # Устанавливаем параметры доски и начальное значение очков для тестов змейки
        self.width_board = 10
        self.height_board = 10
        self.height_score = 0

    def test_separate_no_shovel(self):
        # Тестируем разделение змеи без использования лопат
        # Создаем начальное состояние змеи
        initial_snake = deque([Point(2, 2), Point(2, 3), Point(2, 4)])
        direction = Point(0, 1)
        snake = Snake(initial_snake, direction, self.width_board, self.height_board, self.height_score)
        
        # Определяем пустой список лопат
        shovel = []
        
        # Вызываем метод разделения змеи
        parts = snake.separate(shovel)
        
        # Проверяем, что змейка не разделилась и осталась целой
        self.assertEqual(len(parts), 1)
        self.assertEqual(parts[0].get_len(), 3)

    def test_separate_with_shovel(self):
        # Тестируем разделение змеи с одной лопатой
        # Создаем начальное состояние змеи
        initial_snake = deque([Point(2, 2), Point(2, 3), Point(2, 4)])
        direction = Point(0, 1)
        snake = Snake(initial_snake, direction, self.width_board, self.height_board, self.height_score)
        
        # Определяем лопату на позиции (2, 3)
        shovel = [Point(2, 3)]
        
        # Вызываем метод разделения змеи
        parts = snake.separate(shovel)
        
        # Проверяем, что змейка разделилась на две части
        self.assertEqual(len(parts), 2)
        self.assertEqual(parts[0].get_len(), 1)
        self.assertEqual(parts[1].get_len(), 1)

    def test_separate_with_multiple_shovels(self):
        # Тестируем разделение змеи с несколькими лопатами
        # Создаем начальное состояние змеи
        initial_snake = deque([Point(2, 2), Point(2, 3), Point(2, 4)])
        direction = Point(0, 1)
        snake = Snake(initial_snake, direction, self.width_board, self.height_board, self.height_score)
        
        # Определяем лопаты на позициях (2, 3) и (2, 2)
        shovel = [Point(2, 3), Point(2, 2)]
        
        # Вызываем метод разделения змеи
        parts = snake.separate(shovel)
        
        # Проверяем, что змейка разделилась на одну часть с длиной 1
        self.assertEqual(len(parts), 1)
        self.assertEqual(parts[0].get_len(), 1)

    def test_separate_many_snakes(self):
        # Тестируем разделение большой змеи на несколько частей с использованием лопат
        # Создаем начальное состояние длинной змеи
        initial_snake = deque([
            Point(1, 1), Point(1, 2), Point(1, 3), Point(2, 3), Point(3, 3), 
            Point(3, 2), Point(3, 1), Point(4, 1), Point(4, 2)
        ])
        direction = Point(1, 0)
        snake = Snake(initial_snake, direction, self.width_board, self.height_board, self.height_score)
        
        # Определяем лопаты на позициях (1, 2), (2, 2), и (3, 2)
        shovel = [Point(1, 2), Point(2, 2), Point(3, 2)]
        
        # Вызываем метод разделения змеи
        parts = snake.separate(shovel)
        
        # Проверяем, что змейка разделилась на три части
        self.assertEqual(len(parts), 3)
        self.assertEqual(parts[0].get_len(), 1)
        self.assertEqual(parts[1].get_len(), 3)
        self.assertEqual(parts[2].get_len(), 3)

class TestGameEngine(unittest.TestCase):
    def setUp(self):
        # Устанавливаем параметры игрового движка
        self.width = 40
        self.height = 40
        self.height_score = 0

    def test_change_snakes_direction_normal(self):
        # Тестируем изменение направления змеи в обычных условиях
        # Создаем экземпляр игрового движка и добавляем лужу
        engine = GameEngine(self.width, self.height, self.height_score)
        engine.puddles = [Puddle(self.width, self.height, self.height_score)]
        puddle_pos = engine.puddles[0].p
        
        # Создаем змею, находящуюся рядом с лужей
        engine.snakes = [Snake(deque([Point(puddle_pos.x() + 1, puddle_pos.y() + 1)]), Point(0, 1), self.width, self.height, self.height_score)]
        
        # Определяем новое направление движения змеи
        new_direction = Point(1, 0)
        
        # Вызываем метод изменения направления движения змеи
        engine.change_snakes_direction(new_direction)
        
        # Проверяем, что направление движения змеи изменилось на ожидаемое
        self.assertEqual(engine.snakes[0].get_direction(), Point(1, 0))

    def test_change_snakes_direction_in_puddle(self):
        # Тестируем изменение направления змеи, находящейся в луже
        # Создаем экземпляр игрового движка и добавляем лужу
        engine = GameEngine(self.width, self.height, self.height_score)
        engine.puddles = [Puddle(self.width, self.height, self.height_score)]
        puddle_pos = engine.puddles[0].p
        
        # Создаем змею, находящуюся в луже
        engine.snakes = [Snake(deque([puddle_pos]), Point(0, 1), self.width, self.height, self.height_score)]
        
        # Определяем новое направление движения змеи
        new_direction = Point(1, 0)
        
        # Вызываем метод изменения направления движения змеи
        engine.change_snakes_direction(new_direction)
        
        # Проверяем, что направление движения змеи изменилось на противоположное из-за нахождения в луже
        self.assertEqual(engine.snakes[0].get_direction(), Point(-1, 0))

    def test_change_snakes_direction_multiple_snakes(self):
        # Тестируем изменение направления для нескольких змей, одна из которых находится в луже
        # Создаем экземпляр игрового движка и добавляем лужу
        engine = GameEngine(self.width, self.height, self.height_score)
        engine.puddles = [Puddle(self.width, self.height, self.height_score)]
        puddle_pos = engine.puddles[0].p
        
        # Создаем две змеи, одна из которых находится в луже
        snake1 = Snake(deque([Point(puddle_pos.x() + 1, puddle_pos.y() + 1)]), Point(0, 1), self.width, self.height, self.height_score)
        snake2 = Snake(deque([puddle_pos]), Point(0, 1), self.width, self.height, self.height_score)
        engine.snakes = [snake1, snake2]
        
        # Определяем новое направление движения змей
        new_direction = Point(1, 0)
        
        # Вызываем метод изменения направления движения змей
        engine.change_snakes_direction(new_direction)
        
        # Проверяем, что направление первой змеи изменилось на ожидаемое, а второй - на противоположное из-за нахождения в луже
        self.assertEqual(engine.snakes[0].get_direction(), Point(1, 0))
        self.assertEqual(engine.snakes[1].get_direction(), Point(-1, 0))

    def test_change_snakes_direction_two_puddles_same_position(self):
        # Тестируем изменение направления змеи при наличии двух луж в одной позиции
        # Создаем экземпляр игрового движка и добавляем две лужи на одну и ту же позицию
        engine = GameEngine(self.width, self.height, self.height_score)
        engine.puddles = [Puddle(self.width, self.height, self.height_score), Puddle(self.width, self.height, self.height_score)]
        engine.puddles[1].p = engine.puddles[0].p
        
        # Проверяем, что обе лужи действительно в одной позиции
        self.assertEqual(engine.puddles[0].p, engine.puddles[1].p)
        
        # Создаем змею в той же позиции, что и лужи
        engine.snakes = [Snake(deque([engine.puddles[0].p]), Point(0, 1), self.width, self.height, self.height_score)]
        
        # Определяем новое направление движения змеи
        new_direction = Point(1, 0)
        
        # Вызываем метод изменения направления движения змеи
        engine.change_snakes_direction(new_direction)
        
        # Проверяем, что направление движения змеи изменилось на противоположное из-за нахождения в луже
        self.assertEqual(engine.snakes[0].get_direction(), Point(-1, 0))

class TestSnakeMovement(unittest.TestCase):
    def setUp(self):
        # Устанавливаем параметры доски и начальное значение очков для тестов движения змеи
        self.width_board = 10
        self.height_board = 10
        self.height_score = 1

    def test_move_up(self):
        # Тестируем движение змеи вверх
        # Создаем начальное состояние змеи
        initial_snake = deque([Point(5, 5)])
        direction = Point(0, -1)
        snake = Snake(initial_snake, direction, self.width_board, self.height_board, self.height_score)
        
        # Двигаем змею
        snake.move()
        
        # Ожидаемое новое состояние змеи
        expected_snake = deque([Point(5, 4)])
        
        # Проверяем, что новое состояние змеи соответствует ожидаемому
        self.assertListEqual(list(snake.snake), list(expected_snake))

    def test_move_down(self):
        # Тестируем движение змеи вниз
        # Создаем начальное состояние змеи
        initial_snake = deque([Point(5, 9)])
        direction = Point(0, 1)
        snake = Snake(initial_snake, direction, self.width_board, self.height_board, self.height_score)
        
        # Двигаем змею
        snake.move()
        
        # Ожидаемое новое состояние змеи
        expected_snake = deque([Point(5, 1)])
        
        # Проверяем, что новое состояние змеи соответствует ожидаемому
        self.assertListEqual(list(snake.snake), list(expected_snake))

    def test_move_left(self):
        # Тестируем движение змеи влево
        # Создаем начальное состояние змеи
        initial_snake = deque([Point(0, 5)])
        direction = Point(-1, 0)
        snake = Snake(initial_snake, direction, self.width_board, self.height_board, self.height_score)
        
        # Двигаем змею
        snake.move()
        
        # Ожидаемое новое состояние змеи
        expected_snake = deque([Point(9, 5)])
        
        # Проверяем, что новое состояние змеи соответствует ожидаемому
        self.assertListEqual(list(snake.snake), list(expected_snake))

    def test_move_right(self):
        # Тестируем движение змеи вправо
        # Создаем начальное состояние змеи
        initial_snake = deque([Point(9, 5)])
        direction = Point(1, 0)
        snake = Snake(initial_snake, direction, self.width_board, self.height_board, self.height_score)
        
        # Двигаем змею
        snake.move()
        
        # Ожидаемое новое состояние змеи
        expected_snake = deque([Point(0, 5)])
        
        # Проверяем, что новое состояние змеи соответствует ожидаемому
        self.assertListEqual(list(snake.snake), list(expected_snake))

if __name__ == '__main__':
    unittest.main()
