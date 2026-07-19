def convert(number):
    """Convert a number into its corresponding raindrop sounds.

    Parameters:
        number (int): The number to convert.

    Returns:
        str: The corresponding raindrop sounds, or the number as a string
        if it is not divisible by 3, 5, or 7.

    Rules:
        - If the number is divisible by 3, add "Pling" to the result.
        - If the number is divisible by 5, add "Plang" to the result.
        - If the number is divisible by 7, add "Plong" to the result.
        - If the number is not divisible by 3, 5, or 7, return the number
          as a string.
    """

    result = ""

    if number % 3 == 0:
        result += "Pling"
    elif number % 5 == 0:
        result += "Plang"    
    return result