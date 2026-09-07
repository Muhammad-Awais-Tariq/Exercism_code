def convert(input_grid):
    """Converts the input grid into the numbers.

    Parameters:
        input_grid (list) : The given chracter.
    
    Returns:
        int: The recognized digit.
    """

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")