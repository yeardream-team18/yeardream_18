def simulate_monty_hall(num_simulations, switch):
    """
    Simulates the Monty Hall problem for the specified number of simulations
    with the specified switching strategy.

    Args:
    - num_simulations (int): The number of simulations to run.
    - switch (bool): Whether or not the player will switch doors after the host
      reveals a goat.

    Returns:
    - success_rate (float): The fraction of simulations in which the player
      won the car.
    """

    num_successes = 0

    for i in range(num_simulations):
        # Randomly choose the door behind which the car is located
        car_door = select_door()
       
        # Randomly choose the door that the player selects
        player_door = select_door()
       
        # Randomly choose one of the two doors that the host can reveal
        # (i.e., a door that the player did not select and that does not
        # contain the car)
        revealed_goat_door = reveal_goat_door(car_door, player_door)

        if switch:
             # If the player switches, choose the other unchosen door
            player_door = [d for d in [1, 2, 3] if d != player_door and d != revealed_goat_door][0]
        
        if player_door == car_door:
            num_successes += 1

    success_rate = num_successes / num_simulations

    return success_rate
