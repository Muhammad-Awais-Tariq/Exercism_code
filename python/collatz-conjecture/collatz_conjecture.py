def steps(number):
    """ Return the number of steps required to reach 1 using the Collatz conjecture.

    Parameters:
        number(int): The give number.
    
    Returns:
        int: The number of steps required to reach 1.
    
    Collatz conjecture rules:
        If the number is even, divide it by 2.
        If the number is odd, multiply it by 3 and add 1.
    """
    if number >= 1:
        steps = 0

        while number != 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = (number * 3) + 1
            steps += 1
        
        return steps
    
    else:
        raise ValueError("Only positive integers are allowed")