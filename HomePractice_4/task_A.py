'''# Считываем количество чисел в массиве
N = int(input())
# Считываем сам массив чисел
numbers = list(map(int, input().split()))

# Считываем количество запросов
K = int(input())
# Создаем список для хранения ответов
answers = []

# Обрабатываем каждый запрос
for _ in range(K):
    # Считываем диапазон запроса
    L, R = map(int, input().split())
    # Считаем количество чисел в заданном диапазоне
    count = sum(1 for num in numbers if L <= num <= R)
    answers.append(str(count))

# Выводим ответы в одну строку через пробел
print(' '.join(answers))'''

from collections import Counter

# Считываем количество чисел в массиве
N = int(input())
# Считываем сам массив чисел
numbers = list(map(int, input().split()))

# Подсчитываем количество чисел в каждом диапазоне
num_counts = Counter(numbers)

# Считываем количество запросов
K = int(input())
# Обрабатываем каждый запрос
for _ in range(K):
    # Считываем диапазон запроса
    L, R = map(int, input().split())
    # Получаем количество чисел в заданном диапазоне из предподсчитанных данных
    count = sum(num_counts[num] for num in range(L, R+1))
    print(count, end=' ')