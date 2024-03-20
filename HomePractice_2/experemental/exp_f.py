def fortune_wheel():
    sectors_amount = int(input())

    sectors = list(map(int, input().split()))

    min_velocity, max_velocity, decrease_velocity = map(int, input().split())

    max_sector = 0

    sorted_sectors = sorted(sectors, reverse=True)

    start_sector = sectors[0]

    velocity_range = range(min_velocity, max_velocity+1)

    for index, sector in enumerate(sorted_sectors):
        original_index = sectors.index(sector)

        min_sectors_to_reach_left = sectors_amount - original_index

        min_sectors_to_reach_right = original_index

        min_velocity_to_reach_left = decrease_velocity * min_sectors_to_reach_left + 1

        max_velocity_to_reach_left = decrease_velocity * min_sectors_to_reach_left + 1

        min_velocity_to_reach_right = decrease_velocity * min_sectors_to_reach_right + 1

        max_velocity_to_reach_right = decrease_velocity * min_sectors_to_reach_right + decrease_velocity - 1

        if max_velocity_to_reach_left < min_velocity:
            pass  # Add your logic here

# Call the function to execute
fortune_wheel()