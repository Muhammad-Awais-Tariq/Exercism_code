def roman(number):
    """Convert an Arabic numeral to a Roman numeral.

    Parameters:
        number (int): The Arabic numeral to convert.

    Returns:
        str: The Roman numeral representation.
    """

    roman_map = {
        1 : "I",
        5 : "V",
        10 : "X",
        50 : "L",
        100 : "C",
        500 : "D",
        1000 : "M"
    }

    special_map = {
        4 : "IV",
        9 : "IX",
        40 : "XL",
        90 : "XC",
        400 : "CD",
        900 : "CM"        
    }

    if number in special_map:
        return special_map[number]

    if number in roman_map:
        return roman_map[number]
    