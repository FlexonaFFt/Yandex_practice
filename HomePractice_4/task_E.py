'''def find_fraction(n):
    numerator = 1
    denominator = 1
    count = 1

    while count < n:
        if numerator <= denominator:
            numerator += 1
        else:
            denominator += 1
            numerator = 1
        count += 1

    return numerator, denominator

n = int(input())
numerator, denominator = find_fraction(n)
print(f"{numerator}/{denominator}")'''

'''def find_fraction(n):
    k = int((2*n)**0.5)
    while k*(k+1) // 2 < n:
        k += 1
    d = k*(k+1) // 2 - n
    return f'{k-d}/{d+1}'

n = 2
result = find_fraction(n)
print(result)'''

def find_fraction(n):
    k = int((2*n)**0.5)
    while k*(k+1) // 2 < n:
        k += 1
    d = k*(k+1) // 2 - n
    if k % 2 != 0:
        return f'{k-d}/{d+1}' if d != 0 else f'{k}/{1}'
    else:
        return f'{d+1}/{k-d}' if d != 0 else f'{1}/{k}'

n = int(input())
result = find_fraction(n)
print(result)