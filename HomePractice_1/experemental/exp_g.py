def destroy_barracks():
    amount_of_my_soldiers = int(input())
    barracks_health = int(input())
    amount_of_opponent_soldiers_per_round = int(input())

    amount_of_opponent_soldiers = 0
    my_remaining_soldiers = 0
    opponent_points = barracks_health
    current_round = 0

    while amount_of_my_soldiers > 0 and opponent_points > 0:
        my_remaining_soldiers = amount_of_my_soldiers - min(opponent_points, amount_of_my_soldiers)
        opponent_points -= min(amount_of_my_soldiers, opponent_points)
        amount_of_my_soldiers -= min(amount_of_opponent_soldiers, amount_of_my_soldiers)

        if opponent_points <= amount_of_opponent_soldiers_per_round:
            amount_of_opponent_soldiers += amount_of_opponent_soldiers_per_round
            opponent_points += amount_of_opponent_soldiers

        current_round += 1

    if amount_of_my_soldiers == 0:
        current_round = -1

    print(current_round)

destroy_barracks()
