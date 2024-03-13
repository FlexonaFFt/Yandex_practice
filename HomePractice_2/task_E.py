'''n = int(input())
berries = []
for i in range(n):
    a, b = map(int, input().split())
    berries.append((a, b, i+1))

berries.sort(key=lambda x: x[0] - x[1], reverse=True)

height = 0
order = []
for berry in berries:
    a, b, i = berry
    if height + a > 0:
        height += a
        order.append(i)
    else:
        break

print(height)
print(' '.join(map(str, order)))'''

'''num_ = int(input())
berrier = []
for i in range(num_):
    a, b = map(int, input().split())
    berrier.append((a, b, i+1))

berrier.sort(key=lambda x: (x[0] - x[1], -x[0]), reverse=True)

height = 0
max_height = 0
poryadok = []
for berry in berrier:
    a, b, i = berry
    if height + a > max_height:
        max_height = height + a
    height += a - b
    poryadok.append(i)

print(max_height)
print(' '.join(map(str, poryadok)))'''

'''num_ = int(input())
stopper = []
for i in range(num_):
    a, b = map(int, input().split())
    stopper.append((a, b, i+1))
stopper.sort(key=lambda x: x[0]-x[1], reverse=True)
max_height = 0
por = []
clime, descend = 0, 0
for a, b, i in stopper:
    clime += a
    if clime - descend > max_height:
        max_height = clime - descend
    por.append(i)
    descend += b
print(max_height)
print(*por)'''

# Программа прошла 8 тест!!!
import random

n = int(input())
berries = []
for i in range(n):
    a, b = map(int, input().split())
    berries.append((a, b, i+1))

berries.sort(key=lambda x: (random.random() * 0.5 + 0.5) * (x[0] - x[1]), reverse=True)

max_height = 0
order = []
climb = 0
descend = 0
for a, b, i in berries:
    climb += a
    if climb - descend > max_height:
        max_height = climb - descend
    order.append(i)
    descend += b

print(max_height)
print(*order)