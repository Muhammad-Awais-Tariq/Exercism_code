def triplets_with_sum(number):
    """Return the pythagorean triplet whose sum is equal to the given number.

    Paramters:
        number (int): The number which sum we want.
    
    Returns:
        (list) : The numbers whose sum is equal to the given number 
    """

    numbers = []

    for a in range(1, number-3):
        for b in range(a , number):
            c = number - a - b
            if c > b:
                if (a ** 2) + (b ** 2) == (c** 2):
                    numbers.append([a,b,c])

    return numbers