
COLORS = ["black" , "brown" , "red" , "orange" , "yellow" , "green" , "blue" , "violet" , "grey" , "white"]
TOLERANCE_BAND_VALUES = {
    "grey" : "±0.05%",
    "violet" : "±0.1%",
    "blue" : "±0.25%",
    "green" : "±0.5%",
    "brown" : "±1%",
    "red" : "±2%",
    "gold" : "±5%",
    "silver" : "±10%"
}

def value(colors ,total_values):
    """Return the resistor value represented by the first two colors.

    Parameters:
        colors (list): The resistor color bands.
        total_values (int): How many bands play a role in determining the value.

    Returns:
        int: The resistor value represented by the first two colors.
    """

    color_value = ""

    if len(colors) == 1:
        return int(COLORS.index(colors[0]))
    
    for color_index in range(total_values):
        color_value += str(COLORS.index(colors[color_index]))

    return int(color_value)


def label(colors):
    """Return the resistor's resistance as a formatted label.

    Parameters:
        colors (list): The resistor color bands.

    Returns:
        str: The resistance label, including the appropriate unit.
    """
    total_colors = len(colors)

    if total_colors == 1:
        color_value = value(colors,1)
        full_color_value = color_value   

    elif 2 <= total_colors < 5:
        color_value = value(colors , 2)
        full_color_value = (color_value ) * (10 **COLORS.index(colors[2]))

    else:
        color_value = value(colors , 3)
        full_color_value = (color_value) * (10 **COLORS.index(colors[3]))        

    if not full_color_value:
        return "0 ohms"

    if full_color_value >= 1000000000 :
        return f"{(full_color_value / 1000000000):g} gigaohms"   

    if full_color_value  >= 1000000:
        return f"{(full_color_value / 1000000):g} megaohms"
        
    if full_color_value  >= 1000 :
        return f"{(full_color_value / 1000):g} kiloohms"

    return f"{full_color_value} ohms"


def resistor_label(colors):
    """Return the formatted label for a resistor.

    Parameters:
        colors (list): The four color bands of the resistor.

    Returns:
        str: The resistor's resistance value with the appropriate unit and tolerance.
    """

    resistance_label = label(colors)
    if colors[-1] in TOLERANCE_BAND_VALUES:
        return f"{resistance_label} {TOLERANCE_BAND_VALUES[colors[-1]]}"
    return resistance_label