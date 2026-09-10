def primes(limit):
    """find the prime up to given number using sieve algorithm.

    Parameters:
        limit (int) : the upper limit.

    Returns:
        list : All the prime numbers.
    """

    if limit < 2:
        return []
    
    primes = [num for num in range(2,limit+1)]
    is_prime = [True] * len(primes)

    for idx in range(len(primes)):
       if is_prime[idx] == True:
            for multiple in range(2 , limit):
                if primes[idx] * multiple <= limit:
                        is_prime[primes.index(primes[idx] * multiple)] = False
                else:
                    break

    return [primes[idx] for idx in range(len(primes)) if is_prime[idx] != False]