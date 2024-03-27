W, n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def calc_h(width, mass):
    h = 0
    li = 0
    for x in mass:
        if li == 0:
            if x == width:
                h += 1
                li = 0
            elif x < width:
                li = x
                h += 1
        else:
            if li + x + 1 <= width:
                li += x + 1
            else:
                li = x
                h += 1
    return h

def calc_optimal_width(h, mass):
    width_min = max(mass)
    width_max = sum(mass) + len(mass) + 1
    l = width_min
    r = width_max
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if calc_h(width=m, mass=mass) <= h:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans

def get_min_width(h, mass1, mass2):
    w1 = calc_optimal_width(h=h, mass=mass1)
    h1 = calc_h(width=w1, mass=mass1)
    w2 = calc_optimal_width(h=h, mass=mass2)
    h2 = calc_h(width=w2, mass=mass2)
    return w1 + w2, max(h1, h2)

h_min = 1
h_max = len(A) + len(B) + 1
l = h_min
r = h_max
ans = -1
while l <= r:
    m = (l + r) // 2
    w_test, h_test = get_min_width(h=m, mass1=A, mass2=B)
    if w_test > W:
        l = m + 1
    else:
        ans = h_test
        r = m - 1

print(ans)

'''
Расчет высоты для одной части рапорта:
Функция calc_h(width, mass) вычисляет высоту h для одной части
рапорта, учитывая ширину width и массив длин слов mass.
Используется переменная li для отслеживания текущей длины строки.
Проходя по каждому слову в массиве mass, функция определяет, скол
ько строк потребуется для записи всех слов с учетом ширины.

Расчет оптимальной ширины для одной части рапорта:
Функция calc_optimal_width(h, mass) находит оптимальную 
ширину для одной части рапорта, учитывая высоту h и мас
сив длин слов mass. Определяется минимальная и максимал
ьная возможная ширина. Применяется бинарный поиск для н
ахождения оптимальной ширины, при которой высота не пре
вышает заданное значение h.

Получение минимальной ширины для обеих частей рапорта
Функция get_min_width(h, mass1, mass2) находит минималь
ную ширину для обеих частей рапорта, учитывая заданную 
высоту h и массивы длин слов mass1 и mass2. Для каждой 
части рапорта находится оптимальная ширина и соответст
вующая высота. Возвращается суммарная ширина и максима
льная высота из двух частей.

Решение задачи
Задается минимальная и максимальная высота для обеих ч
астей рапорта. Применяется бинарный поиск для нахожден
ия минимальной высоты, при которой ширина не превышает 
заданное значение W. Выводится найденная минимальная в
ысота, которая удовлетворяет условиям задачи.
'''