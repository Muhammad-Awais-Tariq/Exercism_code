def rows(letter):
    """Draw a diamond pattern based on the given letter.

    Parameters:
        letter (str): The given letter.

    Returns:
        str: The diamond pattern.
    """

    letter_position = ord(letter) - 65
    result = []

    for rows in range(letter_position+1):
        row = ""
        for first_column in range(letter_position-rows):
            row += " "
        row += chr (rows + 65)
        for second_column in range(2 * rows - 1):
            row += " "
        if rows != 0:
            row += chr (rows + 65)
        result.append(row)

    for rows in range(letter_position - 1 , -1 , -1):
        for first_column in range(letter_position-rows):
            print(" " , end=" ")
        print(chr (rows + 65) , end=" ")
        for second_column in range(2 * rows - 1):
            print(" " , end=" ")
        if rows != 0:
            print(chr (rows + 65) , end=" ")
        print()

rows("E")