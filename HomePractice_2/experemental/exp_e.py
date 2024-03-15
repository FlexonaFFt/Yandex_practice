def ambitious_snail():
    number_of_berries = int(input())

    berries = []

    last_positive_berry_index = -1

    for _ in range(number_of_berries):
        berry_params = list(map(int, input().split()))

        berry_strength = berry_params[0] - berry_params[1]
        berry_max_height = berry_params[0]
        berry_number = len(berries) + 1

        berry = (berry_number, berry_strength, berry_max_height)

        berries.append(berry)

    positive_berries, negative_berries = [], []

    for berry in berries:
        if berry[1] > 0:
            positive_berries.append(berry)
        else:
            negative_berries.append(berry)

    if negative_berries:
        max_height_for_berry = max(negative_berries, key=lambda x: x[2])[2]
        berry_to_reach_max_height = min(filter(lambda x: x[2] == max_height_for_berry, negative_berries), key=lambda x: x[1])
        berry_to_reach_max_height_index = negative_berries.index(berry_to_reach_max_height)
        negative_berries[0], negative_berries[berry_to_reach_max_height_index] = negative_berries[berry_to_reach_max_height_index], negative_berries[0]

    max_height = 0

    positive_berry_sum = sum(berry[1] for berry in positive_berries)

    for index, berry in enumerate(positive_berries):
        max_height_if_last = positive_berry_sum - berry[1] + berry[2]

        if max_height_if_last > max_height:
            max_height = max_height_if_last
            last_positive_berry_index = index

    if last_positive_berry_index != -1:
        positive_berries[last_positive_berry_index], positive_berries[-1] = positive_berries[-1], positive_berries[last_positive_berry_index]

    if negative_berries:
        max_height_with_first_negative = sum(berry[1] for berry in positive_berries) + negative_berries[0][2]

        if max_height_with_first_negative > max_height:
            max_height = max_height_with_first_negative

    sorted_berries = positive_berries + negative_berries

    print(max_height)
    print(" ".join(str(berry[0]) for berry in sorted_berries))

ambitious_snail()

'''
Чтение входных данных:
Считывается количество ягод n.
Для каждой ягоды считываются параметры a_i и b_i, 
описывающие насколько улитка поднимается и опускается после съедания ягоды.

Создание списка ягод:
Для каждой ягоды создается кортеж с номером ягоды, 
силой подъема и максимальной высотой.
Ягоды разделяются на положительные (повышающие высоту) 
и отрицательные (понижающие высоту).

Определение максимальной высоты:
Если есть отрицательные ягоды, выбирается та, 
которая позволит достичь максимальной высоты.
Вычисляется максимальная высота, 
если последняя ягода положительная.
Если есть отрицательные ягоды, проверяется 
максимальная высота с первой отрицательной.

Формирование порядка подачи ягод:
Ягоды сортируются по порядку: сначала положительные, затем отрицательные.
Выводится максимальная высота и порядок подачи ягод.
'''