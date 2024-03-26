def count_cells_by_ship_max_size(k):
    total_ship_cells_amount = 0

    if k % 2 == 1:
        n = k // 2 + 1
        total_ship_cells_amount = n * (2 * n - 1) * (2 * n + 1) // 3
    else:
        n = k // 2
        total_ship_cells_amount = 2 * n * (n + 1) * (2 * n + 1) // 3

    sum = total_ship_cells_amount + k * (k - 1) // 2 + (k - 1)
    return sum

def line_warships():
    cells_amount = int(input())
    max_ship_size_left = 0
    max_ship_size_right = cells_amount

    while max_ship_size_left < max_ship_size_right:
        max_ship_size_middle = (max_ship_size_left + max_ship_size_right + 1) // 2
        if count_cells_by_ship_max_size(max_ship_size_middle) <= cells_amount:
            max_ship_size_left = max_ship_size_middle
        else:
            max_ship_size_right = max_ship_size_middle - 1

    print(max_ship_size_left)

def square_sum(k):
    max_number_in_sequence = 2 * k - 1
    return k * (2 * max_number_in_sequence - 1) * (2 * max_number_in_sequence + 1) // 3