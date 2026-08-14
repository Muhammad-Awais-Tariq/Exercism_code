def rows(letter):
    """Return a diamond pattern ending with the given letter.

    Parameters:
        letter (str): The letter at the widest point of the diamond.

    Returns:
        list[str]: The rows of the diamond pattern.
    """

    letter_position = ord(letter) - ord("A")
    result = []

    for row_number in range(letter_position + 1):
        row = ""

        for _ in range(letter_position - row_number):
            row += " "

        row += chr(row_number + ord("A"))

        for _ in range(2 * row_number - 1):
            row += " "

        if row_number != 0:
            row += chr(row_number + ord("A"))

        for _ in range(letter_position - row_number):
            row += " "

        result.append(row)

    for row_number in range(letter_position - 1, -1, -1):
        row = ""

        for _ in range(letter_position - row_number):
            row += " "

        row += chr(row_number + ord("A"))

        for _ in range(2 * row_number - 1):
            row += " "

        if row_number != 0:
            row += chr(row_number + ord("A"))

        for _ in range(letter_position - row_number):
            row += " "

        result.append(row)

    return result