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

    if number != 11 and last_digit == 1:
        postfix = "st"