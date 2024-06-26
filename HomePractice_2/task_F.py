'''def predskazatel(num_, sec, a, b, k):
    max_win = 0
    for i in range(num_):
        for j in range(i, num_):
            now_win = sum(sec[i:j+1])
            if now_win > max_win:
                max_win = now_win
    return max_win'''

'''def predskazatel(n, sectors, a, b, k):
    max_win = 0
    for i in range(n):
        now_speed = a
        now_win = 0
        for j in range(n):
            now_win += sectors[(i+j) % n]
            now_speed = max(a, now_speed - k)
            if now_win > max_win:
                max_win = now_win
    return max_win

num_ = int(input())
sectors = list(map(int, input().split()))
a, b, k = map(int, input().split())
max_win = predskazatel(num_, sectors, a, b, k)
print(max_win)'''

'''def max_win(n, numbers, a, b, k):
    max_win = 0
    for i in range(n):
        if max_win < numbers[i]:
            max_win = numbers[i]
    return max_win - k if max_win - k >= numbers[0] else max_win

n = int(input())
numbers = list(map(int, input().split()))
a, b, k = map(int, input().split())

max_win = max_win(n, numbers, a, b, k)
print(max_win)'''

'''def winner(n, sec, a, b, k):
    max_ = 0
    for i in range(n):
        v = a
        cur_ = sec[i]
        for j in range(i+1, i+n):
            sector = sec[j % n]
            if v <= k:
                break
            cur_ = sector
            v -= k
            v = min(v + 1, b)
        max_ = max(max_, cur_)
    return max_'''

def calculate_max_win(n, sectors, a, b, k):
    na = (a - 1) // k
    nb = (b - 1) // k
    max_win = max(sectors)

    if na + n - 1 >= nb:
        return max_win
    else:
        start_sector = na % n
        end_sector = nb % n
        if start_sector <= end_sector:
            return max(sectors[start_sector:end_sector + 1])
        else:
            return max(sectors[start_sector:] + sectors[:end_sector + 1])

# Чтение входных данных
n = int(input())
sectors = list(map(int, input().split()))
a, b, k = map(int, input().split())

# Вычисление максимального выигрыша
max_win = calculate_max_win(n, sectors, a, b, k)

# Вывод результата
print(max_win)

'''
В последствии решил задачу с помощью кода experemental/exp_e.py
'''