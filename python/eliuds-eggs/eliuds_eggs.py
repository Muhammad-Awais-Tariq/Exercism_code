def egg_count(display_value):
    """Convert the decimal number to binary and count the 1 bits.

    Parameters:
        display_value (int): The decimal number to convert.

    Returns:
        int: The number of 1 bits in the binary representation.
    """

    count = 0
    while display_value > 0:
        remainder = display_value % 2

        if remainder == 1:
            count += 1

        display_value = display_value // 2

    return count