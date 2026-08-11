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

    stack = []

    for char in input_string:
        if char in bracket_match:
            stack.append(char)

        elif char in bracket_match.values():
            if not stack:
                return False

            if bracket_match[stack[-1]] == char:
                stack.pop()
            else:
                return False

    return True if len(stack) == 0 else False