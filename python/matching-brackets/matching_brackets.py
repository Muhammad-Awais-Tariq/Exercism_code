def is_paired(input_string):
    """Check whether all brackets in the input string are balanced.

    Parameters:
        input_string (str): The string to check.

    Returns:
        bool: True if all brackets are balanced, otherwise False.
    """

    if not input_string:
        return True

    bracket_match = {
        "{" : "}",
        "[" : "]",
        "(" : ")"
    }

    bracket_count = 0

    for char in input_string:
        if char in bracket_match.keys():
            bracket_count += 1
        elif char in bracket_match.values():
            bracket_count -= 1

    return True if bracket_count == 0 else False