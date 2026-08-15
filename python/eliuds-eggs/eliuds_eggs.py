def egg_count(display_value):
    """Convert the decimal number to binary and count the 1 bits.

    Parameters:
        display_value (int): The decimal number to convert.

    Returns:
        int: The number of 1 bits in the binary representation.
    """
    
    return list(bin(display_value)[2:]).count("1")