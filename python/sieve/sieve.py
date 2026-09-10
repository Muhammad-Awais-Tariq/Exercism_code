def primes(limit):
    """Find all prime numbers up to the given limit using the Sieve algorithm.

    Parameters:
        limit (int): The upper limit for finding prime numbers.

    Returns:
        list: A list containing all prime numbers up to the limit.
    """
    if limit < 2:
        return []

    prime_numbers = [number for number in range(2, limit + 1)]
    is_prime = [True] * len(prime_numbers)

    for index in range(len(prime_numbers)):
        if is_prime[index]:
            for multiple in range(2, limit):
                if prime_numbers[index] * multiple <= limit:
                    is_prime[
                        prime_numbers.index(prime_numbers[index] * multiple)
                    ] = False
                else:
                    break

    return [
        prime_numbers[index]
        for index in range(len(prime_numbers))
        if is_prime[index]
    ]