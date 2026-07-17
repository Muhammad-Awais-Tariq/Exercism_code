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
