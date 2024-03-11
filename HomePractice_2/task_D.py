def get_adjacent_cells(row, col):
    return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

N = int(input())
cells = []
for _ in range(N):
    row, col = map(int, input().split())
    cells.append((row, col))

perimeter = 0
for cell in cells:
    row, col = cell
    for adj_cell in get_adjacent_cells(row, col):
        if adj_cell not in cells:
            perimeter += 1

print(perimeter)

'''
Определение функции get_adjacent_cells(row, col):
Эта функция принимает координаты строки row и стол
бца col. Возвращает список соседних клеток для зад
анных координат.

Считывание ввода:
Сначала программа считывает количество выпиленных 
клеток N. Затем в цикле считывает координаты кажд
ой выпиленной клетки и добавляет их в список cells.

Вычисление периметра:
Создается переменная perimeter и инициализируется 
нулем. Для каждой клетки из списка cells определя
ются соседние клетки. Если соседняя клетка не нах
одится в списке cells, то увеличивается значение 
переменной perimeter на 1.

'''