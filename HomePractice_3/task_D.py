def check_repeated_numbers(n, k, measurements):
    seen = {}
    
    for i in range(n):
        if measurements[i] in seen and i - seen[measurements[i]] <= k:
            return "YES"
        seen[measurements[i]] = i
    
    return "NO"

n, k = map(int, input().split())
measurements = list(map(int, input().split()))
result = check_repeated_numbers(n, k, measurements)
print(result)

'''
Этот код определяет функцию check_repeated_numbers, 
которая проверяет наличие повторяющихся чисел с рас
стоянием между ними не более k. Затем происходит вв
од данных - количество измерений n, расстояние k и 
сами измерения. После этого вызывается функция для 
проверки наличия повторяющихся чисел и выводится со
ответствующий результат - "YES" если повторяющееся 
число найдено, и расстояние между повторами не прев
ышает k, и "NO" в противном случае.
'''