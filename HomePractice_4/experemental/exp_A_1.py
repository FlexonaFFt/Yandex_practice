def array_search():
    elements_amount = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    answers = []
    queries = int(input())

    for _ in range(queries):
        min_number, max_number = map(int, input().split())
        left_index = 0
        right_index = len(numbers) - 1
        entries_excluded = 0

        while left_index < right_index:
            middle_index = (left_index + right_index) // 2

            if numbers[middle_index] >= min_number:
                right_index = middle_index
            else:
                left_index = middle_index + 1
                entries_excluded += 1

        entries = len(numbers) - entries_excluded
        answers.append(entries)

    print(" ".join(map(str, answers)))

array_search()