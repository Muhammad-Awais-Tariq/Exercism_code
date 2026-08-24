def roman(number):
    """Convert an Arabic numeral to a Roman numeral.

    Parameters:
        number (int): The Arabic numeral to convert.

    Returns:
        str: The Roman numeral representation.
    """

    roman_map = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    if number in roman_map:
        return roman_map[number]