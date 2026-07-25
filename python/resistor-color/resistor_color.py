
COLORS = ["black" , "brown" , "red" , "orange" , "yellow" , "green" , "blue" , "violet" , "grey" , "white"]

def color_code(color):
    """Return the code corresponding to the given color.

    Parameters:
        color (str): The color whose code to return.

    Returns:
        int: The color code.
    """
    return COLORS.index(color)


def colors():
    """Return the list of valid colors.

    Returns:
        list: The list of valid colors.
    """
    return COLORS