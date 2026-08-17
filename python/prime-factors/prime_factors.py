def factors(value):
    """Find the prime factors of a given number.

    Parameters:
        value (int): The number to find the prime factors of.

    Returns:
        list: The prime factors of the number.
    """

    all_factors = []
    required_number = value

    for number in range(2 , value):

        while required_number % number == 0:
            all_factors.append(number)
            required_number //= number

        if required_number == 1:
            return all_factors

    if required_number > 1:
        all_factors.append(required_number)

    return all_factors