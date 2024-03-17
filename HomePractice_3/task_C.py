'''n = int(input())
arr = list(map(int, input().split()))

count_dict = {}
for num in arr:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

to_remove = 0
for num in count_dict:
    if count_dict[num] > 1:
        to_remove += count_dict[num]

print(to_remove)'''

'''numbersAmount = int(input())
numbers = list(map(int, input().split()))
numbersMap = {k: v for k, v in {k: numbers.count(k) for k in numbers}.items()}
numbersToDelete = 10 ** 8

for number in set(numbers):
    numbersOfCurrent = numbersMap.get(number, 0)
    numbersPlusOne = numbersMap.get(number + 1, 0)
    numbersMinusOne = numbersMap.get(number - 1, 0)

    currentNumbersToDelete = numbersAmount - numbersOfCurrent - max(numbersMinusOne, numbersPlusOne)

    if currentNumbersToDelete < numbersToDelete:
        numbersToDelete = currentNumbersToDelete

print(numbersToDelete)'''

from collections import Counter

numbersAmount = int(input())
numbers = list(map(int, input().split()))
numbersMap = Counter(numbers)
numbersToDelete = 10 ** 8

for number, count in numbersMap.items():
    currentNumbersToDelete = numbersAmount - count - max(numbersMap.get(number - 1, 0), numbersMap.get(number + 1, 0))

    if currentNumbersToDelete < numbersToDelete:
        numbersToDelete = currentNumbersToDelete

print(numbersToDelete)

'''
Подготовка данных:
Создается словарь numbersMap, где ключами являются 
уникальные числа из массива, а значениями их часто
та в массиве.

Нахождение минимального количества чисел для удаления:
Инициализируется переменная numbersToDelete с большим 
значением. Для каждого уникального числа в множестве ч
исел: Получаем количество текущего числа, числа на еди
ницу больше и на единицу меньше из словаря numbersMap.
Вычисляем сколько чисел нужно удалить, чтобы попарная 
разность оставшихся чисел не превышала 1. Обновляем nu
mbersToDelete, если текущее количество для удаления ме
ньше предыдущего минимального.
'''

'''
Оптимизированное решение для нахождения минимального ко
личества чисел:

Вместо создания словаря numbersMap можно использовать 
Counter из модуля collections, что упростит подсчет час
тоты чисел.

Можно избежать лишних итераций по уникальным числам, пе
ребирая только те числа, которые могут влиять на минима
льное количество чисел для удаления.
'''