def rectangles(strings):
    """Count the number of complete rectangles in an ASCII diagram.

    Parameters:
        strings (list[str]): Rows of the ASCII diagram.

    Returns:
        int: The total number of complete rectangles.
    """

    if len(strings) <= 1:
        return 0

    total_rectangles = 0

    for top_row in range(len(strings)):
        for left_column in range(len(strings[top_row])):
            if strings[top_row][left_column] == "+":
                for right_column in range(
                    left_column + 1, len(strings[top_row])
                ):
                    if strings[top_row][right_column] == "+":
                        for bottom_row in range(top_row + 1, len(strings)):
                            if (
                                strings[bottom_row][left_column] == "+"
                                and strings[bottom_row][right_column] == "+"
                            ):
                                valid = True

                                for column in range(
                                    left_column + 1, right_column
                                ):
                                    if strings[top_row][column] not in "-+":
                                        valid = False

                                for column in range(
                                    left_column + 1, right_column
                                ):
                                    if strings[bottom_row][column] not in "-+":
                                        valid = False

                                for row in range(top_row + 1, bottom_row):
                                    if strings[row][left_column] not in "|+":
                                        valid = False

                                    if strings[row][right_column] not in "|+":
                                        valid = False

                                if valid:
                                    total_rectangles += 1

    return total_rectangles