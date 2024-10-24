def printfield(field):
    """Отображает игровое поле, где 0 - пусто, 1 - игрок 1, 2 - игрок 2, 3 - игрок 3."""
    for row in field:
        print(''.join(['.' if cell == 0 else str(cell) for cell in row]))

def straf(field):
    """Считает штрафные очки для игроков на основе соседних фишек."""
    penalties = [0, 0, 0]  # Штрафы для 3 игроков
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # Все направления

    # Для каждого игрока
    for player in range(1, 4):
        for row in range(4):
            for col in range(5):
                if field[row][col] == player:  # Если клетка игрока
                    for dr, dc in directions:  # Проверяем всех соседей
                        r, c = row + dr, col + dc
                        if 0 <= r < 4 and 0 <= c < 5 and field[r][c] == player:
                            penalties[player - 1] += 1  # Увеличиваем штраф

    return [p // 2 for p in penalties]  # Делим на 2, чтобы избежать двойного учета

def endgame(field):
    """Проверяет, остались ли пустые клетки на поле."""
    return all(cell != 0 for row in field for cell in row)  # Если пустых клеток нет, игра окончена

# Основная часть игры
field = [[0] * 5 for _ in range(4)]  # Создаем пустое поле 4x5
player = 1  # Начинаем с игрока 1

while True:
    print(f'Ход игрока {player}')
    while True:
        try:
            x, y = map(int, input('Введите координаты X Y (например, 1 1): ').split())
            if 1 <= x <= 4 and 1 <= y <= 5 and field[x - 1][y - 1] == 0:  # Проверка на допустимость хода
                field[x - 1][y - 1] = player  # Устанавливаем фишку
                break
            print('Некорректный ход, повторите')
        except ValueError:
            print('Некорректный ввод, попробуйте снова.')

    printfield(field)  # Выводим текущее состояние поля

    if endgame(field):  # Проверяем, закончилась ли игра
        break
    
    player = player + 1 if player < 3 else 1  # Переход к следующему игроку

penalties = straf(field)  # Подсчитываем штрафные очки
min_penalty = min(penalties)  # Находим минимальные штрафные очки
print('Штрафные очки:', penalties)  # Выводим штрафные очки
winners = [i + 1 for i, p in enumerate(penalties) if p == min_penalty]  # Находим победителей
print('Победил игрок:', *winners)  # Выводим номера победителей