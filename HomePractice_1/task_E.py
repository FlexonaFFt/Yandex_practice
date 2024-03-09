'''
n, k, d = map(int, input().split())
num = next((i for i in range(10) if (10 * n + i) % k == 0), 1)
print((str(10 * n + num) + '0' * (d - 1)) if num != -1 else -1)'''

n, k, d = map(int, input().split())
# Ищем первую цифру, которую можно добавить к числу n, чтобы результат делился на k
for i in range(10):
    if (10 * n + i) % k == 0:
        num = i
        break
else:
    num = -1

# Формируем ответ: число через d дней
if num != -1:
    result = str(10 * n + num) + '0' * (d - 1)
else:
    result = -1

print(result)