'''
vasya_tree, vasya_range = map(int, input().split())
masha_tree, masha_range = map(int, input().split())
counter_1, counter_2 = 0, 0
for _ in range(vasya_tree - vasya_range, vasya_tree + vasya_range + 1):
    counter_1 += 1
for _ in range(masha_tree - masha_range, masha_tree + masha_range + 1):
    counter_2 += 1
vasya_movement = range(vasya_tree - vasya_range, vasya_tree + vasya_range + 1)
masha_movement = range(masha_tree - masha_range, masha_tree + masha_range + 1)
public_movement = counter_1 + counter_2
print(public_movement) '''

"""
# Считываем входные данные
vasya_tree, vasya_range = map(int, input().split())
masha_tree, masha_range = map(int, input().split())

# Определяем диапазон для покраски деревьев
start_tree = min(vasya_tree - vasya_range, masha_tree - masha_range)
end_tree = max(vasya_tree + vasya_range, masha_tree + masha_range)

# Вычисляем количество деревьев, которые могут быть покрашены
painted_trees = end_tree - start_tree + 1

# Выводим результат
print(painted_trees)"""

p, v = map(int, input().split())
q, m = map(int, input().split())

print(2 * (v + m + 1) - max([0, min([p + v, q + m]) - max([p - v, q - m]) + 1]))