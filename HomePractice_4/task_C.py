'''def solve(n, m, a, l, s):
    dp = [[0 for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(s+1):
            if j >= a[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-a[i-1]]
    for _ in range(m):
        print(l, s, end=' ')
        if dp[l][s] > 0:
            print(l)
        else:
            print(-1)

n, m = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(m):
    l, s = map(int, input().split())
    solve(n, m, a, l, s)'''

import sys

n, m = map(int, sys.stdin.readline().split())
orc_counts = list(map(int, sys.stdin.readline().split()))


prefix_sum = [0] * (n + 1)
for i, orc_count in enumerate(orc_counts):
    prefix_sum[i + 1] = prefix_sum[i] + orc_count

def binary_search(l, s):
    left, right = 0, n - l
    while left <= right:
        mid = (left + right) // 2
        if prefix_sum[mid + l] - prefix_sum[mid] == s:
            return mid + 1
        elif prefix_sum[mid + l] - prefix_sum[mid] < s:
            left = mid + 1
        else:
            right = mid - 1
    return -1

for _ in range(m):
    l, s = map(int, sys.stdin.readline().split())
    result = binary_search(l, s)
    sys.stdout.write(str(result) + '\n')

'''
Сначала считываются два целых числа n и m из стандартного 
потока ввода, представленного модулем sys.

Затем считывается список orc_counts, содержащий количество
орков в каждом полке.

Создается список prefix_sum, в котором каждый элемент пред
ставляет собой сумму орков до данного полка.

Определяется функция binary_search(l, s), которая выполняе
т бинарный поиск для нахождения начального полка для вылаз
ки.

Для каждого запроса из m строк считываются значения l и s,
и вызывается функция binary_search(l, s) для определения о
твета.

Результаты выводятся в стандартный поток вывода с помощью 
sys.stdout.write.
'''