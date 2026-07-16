def is_armstrong_number(number):
    """Determine whether a given number is an Armstrong number.

    Parameters:
        number (int): The given number.

    Returns:
        bool: True if the number is an Armstrong number; otherwise, False.

    An Armstrong number is a number that is the sum of its own digits,
    each raised to the power of the number of digits.
    """

    digits = [int(d) for d in str(number)]
    sum_of_digits = sum(n**(len(digits)) for n in digits)

    return number == sum_of_digits

