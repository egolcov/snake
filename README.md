1. **Управление змейками**:
   - **Пользователь нажимает**: клавиши W, A, S, D для управления каждой змейкой.
   - **Приложение отображает**: изменение направления движения змейки в соответствии с нажатыми клавишами. Если змейка находится в луже, ее направление меняется на противоположное.

2. **Движение змейки**:
   - **Алгоритм**:
     - При каждом вызове метода `move()`, змейка добавляет новую голову в направлении движения и удаляет последний элемент (хвост).
     - Новая голова рассчитывается как смещение от старой головы на вектор направления.
     - Координаты ограничены размерами игрового поля, что предотвращает выход за его пределы.

3. **Поедание яблок**:
   - **Алгоритм**:
     - При каждом вызове метода `update()`, проверяется столкновение головы змейки с яблоком.
     - Если столкновение произошло, яблоко удаляется из списка, змейка увеличивается в размере, и генерируется новое яблоко и камень.

4. **Растекание лужи**:
   - **Алгоритм**:
     - Лужа моделируется как круг с изменяющимся радиусом, который увеличивается и уменьшается в зависимости от времени.
     - При каждом вызове метода `draw()`, проверяется, достиг ли радиус лужи следующего значения из списка `puddle_radius`.
     - Если достиг, радиус меняется, и лужа перерисовывается с новым радиусом.
     - Если радиус становится нулевым, лужа считается исчезнувшей.

5. **Управление несколькими змейками**:
   - **Пользователь нажимает**: клавиши W, A, S, D для каждой змейки по отдельности.
   - **Приложение отображает**: изменение направления движения каждой змейки в зависимости от нажатых клавиш.

6. **Разделение змейки лопатой**:
   - **Алгоритм**:
     - При столкновении змейки с лопатой, змейка разделяется на части, каждая из которых становится новой змейкой.
     - Лопата рисуется на экране и постепенно исчезает, если время жизни лопаты превышает 2 секунды.

7. **Столкновение с препятствиями (камнями)**:
   - **Алгоритм**:
     - При каждом вызове метода `update()`, проверяется столкновение головы змейки с камнем.
     - Если столкновение произошло, змейка удаляется из списка активных змеек.

8. **Окончание игры**:
   - **Алгоритм**:
     - Игра заканчивается, когда все змейки погибают (столкновение с препятствиями, самопересечение или исчезание).
     - Приложение отображает сообщение "GAME OVER" и предлагает нажать клавишу 'R' для перезапуска игры.
## Описание функциональных моеделей
[functions.md](./docs/functions.md)
## Описание структурных моделей
[struct.md](./docs/struct.md)
