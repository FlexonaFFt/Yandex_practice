def count_cells_by_ship_max_size(k):
    total_ship_cells_amount = 0

    if k % 2 == 1:
        n = k // 2 + 1
        total_ship_cells_amount = n * (2 * n - 1) * (2 * n + 1) // 3
    else:
        n = k // 2
        total_ship_cells_amount = 2 * n * (n + 1) * (2 * n + 1) // 3

    sum = total_ship_cells_amount + k * (k - 1) // 2 + (k - 1)
    return sum

def line_warships():
    cells_amount = int(input())
    max_ship_size_left = 0
    max_ship_size_right = cells_amount

    while max_ship_size_left < max_ship_size_right:
        max_ship_size_middle = (max_ship_size_left + max_ship_size_right + 1) // 2
        if count_cells_by_ship_max_size(max_ship_size_middle) <= cells_amount:
            max_ship_size_left = max_ship_size_middle
        else:
            max_ship_size_right = max_ship_size_middle - 1

    print(max_ship_size_left)

line_warships()

'''
Определение функции count_cells_by_ship_max_size(k):
Функция принимает параметр k, который представляет р
азмер корабля. Вычисляется общее количество клеток, 
занимаемых кораблями заданного размера. Если k нечет
ное, то n = k // 2 + 1 и используется формула для вы
числения клеток. Если k четное, то n = k // 2 и прим
еняется другая формула. Затем вычисляется сумма обще
го количества клеток, занимаемых кораблями заданного 
размера, и дополнительных клеток. 
Возвращается общая сумма.

Определение функции line_warships():
Считывается количество клеток cells_amount. Устанавл
иваются начальные значения для максимального размера 
корабля слева и справа. Пока левый размер корабля ме
ньше правого: Вычисляется средний размер корабля. Ес
ли общее количество клеток, занимаемых кораблями зад
анного размера, меньше или равно cells_amount, то об
новляется левый размер. Иначе обновляется правый раз
мер. Выводится максимальный размер корабля, который 
можно разместить.
'''