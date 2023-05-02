import random

def select_door():
    """
    Randomly selects a door number between 1 and 3.
    """
    return random.randint(1, 3)

def reveal_goat_door(car_door, selected_door):
    """
    Randomly selects a door to reveal that is neither the car door nor the selected door.

    Args:
    - car_door (int): The door number behind which the car is located.
    - selected_door (int): The door number selected by the player.

    Returns:
    - goat_door (int): The door number revealed to the player that contains a goat.
    """
    doors = [1, 2, 3]
    if car_door == selected_door:
        doors.remove(car_door)
        return random.choice(doors)
    else:
        doors.remove(car_door)
        doors.remove(selected_door)
        return doors[0]


