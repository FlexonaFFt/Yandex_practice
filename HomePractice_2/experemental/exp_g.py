def no_more_no_less():
    num_of_test_data = int(input())

    for _ in range(num_of_test_data):
        test_data_size = int(input())
        test_data_list = list(map(int, input().split()))

        sublist_sizes = []  # размеры подмножеств
        current_sublist_length = 0
        possible_sublist_length = 0

        for index, item in enumerate(test_data_list):
            if item < possible_sublist_length or possible_sublist_length == 0:
                possible_sublist_length = item

            current_sublist_length += 1

            if current_sublist_length == possible_sublist_length or item < current_sublist_length or index == len(test_data_list) - 1:
                sub_list_length_to_add = current_sublist_length - 1 if item < current_sublist_length else current_sublist_length
                sublist_sizes.append(sub_list_length_to_add)
                possible_sublist_length = 0
                current_sublist_length = 0

        print(len(sublist_sizes))
        print(" ".join(map(str, sublist_sizes)))

no_more_no_less()
