def simulate_monty_hall(num_simulations, switch):

    num_successes = 0

    for i in range(num_simulations):
        car_door = select_door()

        player_door = select_door()

        revealed_goat_door = reveal_goat_door(car_door, player_door)

        if switch:
            player_door = [d for d in [1, 2, 3] if d != player_door and d != revealed_goat_door][0]

        if player_door == car_door:
            num_successes += 1

    success_rate = num_successes / num_simulations

    return success_rate
