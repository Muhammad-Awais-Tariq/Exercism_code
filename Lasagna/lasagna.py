
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elpased_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return int(EXPECTED_BAKE_TIME - elpased_bake_time)

def preparation_time_in_minutes(number_of_layers):
    """Calculate the prepration time for each layer.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
    
    Returns:
        int: The total prepration time based on the number of the layers and prepration time.

    This function takes in a single integer that is the number of layers if lasagna
    and returns the prepration time for each layer that is (prepration_time_per_layer * no of layers)
    """
    return PREPARATION_TIME * number_of_layers



