
COLORS = ["black" , "brown" , "red" , "orange" , "yellow" , "green" , "blue" , "violet" , "grey" , "white"]

def value(colors):
    """Return the resistor value represented by the first two colors.

    Parameters:
        colors (list): The resistor color bands.

    Returns:
        int: The resistor value represented by the first two colors.
    """

    color_value = ""

    for color_index in range(2):
        color_value += str(COLORS.index(colors[color_index]))

    return int(color_value)


def label(colors):
    """Return the resistor's resistance as a formatted label.

    Parameters:
        colors (list): The resistor color bands.

    Returns:
        str: The resistance label, including the appropriate unit.
    """

    color_value = value(colors[:2])
    full_color_value = (color_value) * (10 **COLORS.index(colors[2]))

    if full_color_value % 1000 == 0:
        return f"{(full_color_value // 1000)} kiloohms"

    return f"{full_color_value} ohms"