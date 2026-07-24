def is_valid(isbn):
    """Check if the given number is an valid isbn number.

    Parameters:
        isbn (str): The number to check.

    Returns:
        bool: True if the number is an isbn, otherwise False.
    """
    formatted_number = isbn.replace("-" , "")[::-1]

    if len(formatted_number) != 10:
        return False

    if "X" in formatted_number:
        if formatted_number.find("X") != 0:
            return False

        if formatted_number.count("X") != 1:
            return False

    sum_number = 0

    for multiplier in range(1,11):
        number = formatted_number[multiplier-1]
        if number.isdigit():
            number = int(number)
        else:
            if number == "X":
                number = 10
            else:
                return False       
        sum_number += multiplier * number
    
    return sum_number % 11 == 0