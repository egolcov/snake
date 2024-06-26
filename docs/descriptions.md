# Перечень тестов

## Модуль примера (snake)

### 1. Метод `snake.separate()`

#### Тест №1.1: Разделение без лопатки (позитивный)
* _Цель_: Проверка разделения змеи при отсутствии лопаток.
* _Входные данные_: Пустой список лопаток.
* _Ожидаемый результат_: Змея не разделяется, оставаясь одной частью длиной 3.
* _Описание процесса_: Вызов метода `separate` с пустым списком лопаток, проверка, что возвращаемый список частей змеи состоит из одной части длиной 3.

#### Тест №1.2: Разделение с одной лопаткой (позитивный)
* _Цель_: Проверка разделения змеи при наличии одной лопатки.
* _Входные данные_: Список с одной лопаткой, расположенной на одной из точек змеи.
* _Ожидаемый результат_: Змея разделяется на две части, каждая длиной 1.
* _Описание процесса_: Вызов метода `separate` с одной лопаткой, проверка, что возвращаемый список частей змеи состоит из двух частей, каждая длиной 1.

#### Тест №1.3: Разделение с двумя лопатками (позитивный)
* _Цель_: Проверка разделения змеи при наличии двух лопаток.
* _Входные данные_: Список с двумя лопатками, расположенными на двух точках змеи.
* _Ожидаемый результат_: Змея разделяется на одну часть длиной 1.
* _Описание процесса_: Вызов метода `separate` с двумя лопатками, проверка, что возвращаемый список частей змеи состоит из одной части длиной 1.

#### Тест №1.4: Разделение сложной змеи с несколькими лопатками (позитивный)
* _Цель_: Проверка разделения сложной змеи с несколькими лопатками.
* _Входные данные_: Змея сложной формы и список с несколькими лопатками.
* _Ожидаемый результат_: Змея разделяется на три части с разной длиной.
* _Описание процесса_: Вызов метода `separate` со сложной змеей и тремя лопатками, проверка, что возвращаемый список частей змеи состоит из трех частей с длиной 1, 3 и 3 соответственно.

## Модуль примера (game_engine)

### 2. Метод `game_engine.change_snakes_direction()`

#### Тест №2.1: Изменение направления движения змеи в обычных условиях (позитивный)
* _Цель_: Проверка изменения направления движения змеи, когда она не находится в луже.
* _Входные данные_: Змея вне лужи, новое направление.
* _Ожидаемый результат_: Направление движения змеи меняется на заданное.
* _Описание процесса_: Создание змеи в обычной позиции, вызов метода `change_snakes_direction` с новым направлением, проверка, что направление змеи изменилось на новое значение.

#### Тест №2.2: Изменение направления движения змеи в луже (позитивный)
* _Цель_: Проверка изменения направления движения змеи, когда она находится в луже.
* _Входные данные_: Змея в луже, новое направление.
* _Ожидаемый результат_: Направление движения змеи меняется на противоположное заданному.
* _Описание процесса_: Создание змеи в позиции лужи, вызов метода `change_snakes_direction` с новым направлением, проверка, что направление змеи изменилось на противоположное значение.

#### Тест №2.3: Изменение направления движения для нескольких змей (позитивный)
* _Цель_: Проверка изменения направления движения для нескольких змей, одна из которых находится в луже.
* _Входные данные_: Две змеи, одна вне лужи, другая в луже, новое направление.
* _Ожидаемый результат_: Направление первой змеи меняется на заданное, направление второй змеи меняется на противоположное заданному.
* _Описание процесса_: Создание двух змей, одна из которых находится в луже, вызов метода `change_snakes_direction` с новым направлением, проверка, что направление первой змеи изменилось на новое значение, а второй – на противоположное.

#### Тест №2.4: Изменение направления движения змеи при наличии двух луж в одной позиции (позитивный)
* _Цель_: Проверка изменения направления движения змеи при наличии двух луж в одной и той же позиции.
* _Входные данные_: Две лужи в одной позиции, змея в той же позиции, новое направление.
* _Ожидаемый результат_: Направление движения змеи меняется на противоположное заданному.
* _Описание процесса_: Создание двух луж в одной позиции, проверка их расположения, создание змеи в той же позиции, вызов метода `change_snakes_direction` с новым направлением, проверка, что направление змеи изменилось на противоположное значение.

### 3. Метод `snake.move()`

#### Тест №3.1: Перемещение вверх (позитивный)
* _Цель_: Проверка перемещения змеи в направлении вверх.
* _Входные данные_: Начальное состояние змеи на позиции (5, 5) и направление вверх (0, -1).
* _Ожидаемый результат_: Змея перемещается на позицию (5, 4).
* _Описание процесса_: Создание змеи с начальным состоянием и направлением вверх, вызов метода `move`, проверка, что новое состояние змеи соответствует ожидаемому.

#### Тест №3.2: Перемещение вниз (позитивный)
* _Цель_: Проверка перемещения змеи в направлении вниз.
* _Входные данные_: Начальное состояние змеи на позиции (5, 9) и направление вниз (0, 1).
* _Ожидаемый результат_: Змея перемещается на позицию (5, 1) (учитывая, что доска циклична по высоте).
* _Описание процесса_: Создание змеи с начальным состоянием и направлением вниз, вызов метода `move`, проверка, что новое состояние змеи соответствует ожидаемому.

#### Тест №3.3: Перемещение влево (позитивный)
* _Цель_: Проверка перемещения змеи в направлении влево.
* _Входные данные_: Начальное состояние змеи на позиции (0, 5) и направление влево (-1, 0).
* _Ожидаемый результат_: Змея перемещается на позицию (9, 5) (учитывая, что доска циклична по ширине).
* _Описание процесса_: Создание змеи с начальным состоянием и направлением влево, вызов метода `move`, проверка, что новое состояние змеи соответствует ожидаемому.

#### Тест №3.4: Перемещение вправо (позитивный)
* _Цель_: Проверка перемещения змеи в направлении вправо.
* _Входные данные_: Начальное состояние змеи на позиции (9, 5) и направление вправо (1, 0).
* _Ожидаемый результат_: Змея перемещается на позицию (0, 5) (учитывая, что доска циклична по ширине).
* _Описание процесса_: Создание змеи с начальным состоянием и направлением вправо, вызов метода `move`, проверка, что новое состояние змеи соответствует ожидаемому.

### Пользовательский интерфейс

#### Выход из игры через системный крестик окна

**Сценарий:** Пользователь нажимает системный крестик в окне игры для выхода из приложения. Приложение завершает текущую сессию игры и закрывает окно.

**Шаги:**

1. Запустить игру.
2. Нажать системный крестик в правом верхнем углу окна игры.
3. Проверить, что игра завершается и окно приложения закрывается.

**Ожидаемый результат:** Игра корректно завершается, и окно приложения закрывается при нажатии системного крестика в окне игры.

---

#### Перезапуск игры после завершения

**Сценарий:** Пользователь нажимает клавишу "R" для перезапуска игры после ее завершения.

**Шаги:**

1. Дождаться окончания игры, когда все змеи погибнут.
2. Нажать клавишу "R".
3. Проверить, что игра перезапускается и начинается новая сессия.

**Ожидаемый результат:** Игра успешно перезапускается при нажатии клавиши "R", и пользователь может начать новую игру.
