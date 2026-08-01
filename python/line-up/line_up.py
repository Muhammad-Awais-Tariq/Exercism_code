def line_up(name, number):
    """Return a personalized greeting based on a customer's name and number.

    Parameters:
        name (str): The customer's name.
        number (int): The customer's number.

    Returns:
        str: A personalized greeting with the correct ordinal suffix.

    Rules:
        - Numbers ending in 1 (except those ending in 11) use "st".
        - Numbers ending in 2 (except those ending in 12) use "nd".
        - Numbers ending in 3 (except those ending in 13) use "rd".
        - All other numbers use "th".
    """

    last_digit = number % 10
    last_num = number % 100

    if last_num != 11 and last_digit == 1:
        postfix = "st"

    elif last_num != 12 and last_digit == 2:
        postfix = "nd"

    elif last_num != 13 and last_digit == 3:
        postfix = "rd"

    else:
        postfix = "th"

    return f"{name}, you are the {number}{postfix} customer we serve today. Thank you!"