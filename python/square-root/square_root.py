def square_root(number):
    """Find the square root of the number using the linear method.

    Parameters:
        number (int): The number that we want the square root of.

    Returns:
        int: The square root of the number.

    Raises:
        ValueError: If no square root is found for the whole number.

    """

    if number == 0:
        return 0

    initial_guess = 1

    while initial_guess * initial_guess != number:

        if initial_guess * initial_guess > number:
            raise ValueError("No square root found")

        initial_guess += 1

    return initial_guess