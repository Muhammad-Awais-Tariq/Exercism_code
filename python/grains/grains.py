def square(number):
    """ Returns the number of grains on a give square
    
    Parameters:
        number(int) : The square of the chessboard
    
    Return:
        int: The number of grains on the given square.
    """
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")    


def total():
    """ Returns the total number of grains on the chess board.
    
    Parameters:
        None
    
    Return:
        int: Total number of grains on the chess board.
    """   
    return sum(square(number) for number in range(1 , 65)) 