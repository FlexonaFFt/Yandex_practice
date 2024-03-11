def ambitious_snail():
    number_of_berries = int(input())

    berries = []

    for i in range(number_of_berries):
        berry_params = list(map(int, input().split()))

        berry_strength = berry_params[0] - berry_params[1]
        berry_max_height = berry_params[0]
        berry_number = i + 1

        berry = (berry_number, berry_strength, berry_max_height)
        berries.append(berry)

    berries.sort(key=lambda x: x[1], reverse=True)

    berries_with_positive_strength = [berry for berry in berries if berry[1] > 0]

    print(f"berries = {berries}")

    extra_height = berries[berries_with_positive_strength[-1][0]][2] if len(berries_with_positive_strength) < len(berries) else 0

    print(f"extraHeight = {extra_height}")

    max_height = sum(berry[1] for berry in berries_with_positive_strength) + extra_height

    print(max_height)

    print(" ".join(str(berry[0]) for berry in berries))

ambitious_snail()
