# начальные координаты
x_l, y_u, x_r, y_d = 10**9, -10**9, -10**9, 10**9

for _ in range(int(input())):
    X, Y = map(int, input().split())
    x_l = min(X, x_l)
    y_d = min(Y, y_d)
    x_r = max(X, x_r)
    y_u = max(Y, y_u)
print(x_l, y_d, x_r, y_u)