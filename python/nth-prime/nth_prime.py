
def is_prime(number):
    """Check whether the given number is prime.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """

    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for devisor in range(3 , int(number ** 0.5) + 1 , 2 ):
        if number % devisor == 0:
            return False

    return True


def prime(number):
    """Return the nth prime number.

    Parameters:
        number (int): The position of the prime number to find (1-indexed).

    Returns:
        int: The nth prime number.

    Raises:
        ValueError: If number is less than 1.
    """

    if number <= 0:
        raise ValueError('there is no zeroth prime')

    primes = []
    prime = 2

    while len(primes) != number:
        if is_prime(prime):
            primes.append(prime)
        prime +=1

    return primes