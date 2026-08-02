def square_of_sum(number):
    """Return the square of the sum of all natural numbers up to the given number.

    Parameters:
        number (int): The upper limit of the natural numbers to sum.

    Returns:
        int: The square of the sum.
    """

    return sum(x for x in range(number + 1)) ** 2


def sum_of_squares(number):
    """Return the sum of the squares of all natural numbers up to the given number.

    Parameters:
        number (int): The upper limit of the natural numbers.

    Returns:
        int: The sum of the squares.
    """

    return sum(x ** 2 for x in range(number + 1))


def difference_of_squares(number):
    """Return the difference between the square of the sum and the sum of the squares of all natural numbers up to the given number.

    Parameters:
        number (int): The upper limit of the natural numbers.

    Returns:
        int: The difference between the square of the sum and the sum of the squares.
    """
    
