def primes(limit):
    """find the prime up to given number using sieve algorithm.

    Parameters:
        limit (int) : the upper limit.

    Returns:
        list : All the prime numbers.
    """

    if limit < 2:
        return []
    
    primes = [2]

    for num in range(3,limit+1):
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
