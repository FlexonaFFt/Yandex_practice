numbersMap = {}

for _ in range(3):
    numbersAmount = int(input())
    numbersSet = set(map(int, input().split()))

    for number in numbersSet:
        numbersAmount = numbersMap.get(number, 0)
        numbersMap[number] = numbersAmount + 1

answerNumbers = ' '.join(map(str, sorted([key for key, value in numbersMap.items() if value > 1])))
print(answerNumbers)

'''
Создается пустой словарь numbersMap, который будет 
использоваться для подсчета количества вхождений к
аждого числа. Далее, для каждого из трех списков:

Считывается количество чисел в списке (numbersAmount).
Считывается сам список чисел как множество (numbersSet), 
чтобы избежать повторяющихся значений.
Для каждого числа в numbersSet увеличивается счетчик в 
словаре numbersMap.

После обработки всех трех списков, формируется строка 
answerNumbers, содержащая отсортированные числа, кото
рые встречаются хотя бы в двух списках (с количеством 
вхождений больше 1).

Наконец, выводится строка answerNumbers, содержащая на
йденные числа через пробел.
'''