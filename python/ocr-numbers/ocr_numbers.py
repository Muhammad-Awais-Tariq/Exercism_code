def convert(input_grid):
    """Convert an OCR grid into a string of recognized digits.

    Parameters:
        input_grid (list): The OCR grid containing digit patterns.

    Returns:
        str: The recognized digits, with commas separating groups.

    Raises:
        ValueError: If the number of input lines is not a multiple of four
            or the number of input columns is not a multiple of three.
    """

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    pattern_dict = {
        (" _ ", "| |", "|_|", "   "): "0",
        ("   ", "  |", "  |", "   "): "1",
        (" _ ", " _|", "|_ ", "   "): "2",
        (" _ ", " _|", " _|", "   "): "3",
        ("   ", "|_|", "  |", "   "): "4",
        (" _ ", "|_ ", " _|", "   "): "5",
        (" _ ", "|_ ", "|_|", "   "): "6",
        (" _ ", "  |", "  |", "   "): "7",
        (" _ ", "|_|", "|_|", "   "): "8",
        (" _ ", "|_|", " _|", "   "): "9",
    }

    if len(input_grid[0]) == 3:
        try:
            return pattern_dict[tuple(input_grid)]
        except KeyError:
            return "?"

    if len(input_grid) > 4:
        full_final_word = ""

        for group_start in range(0, len(input_grid), 4):
            current_group = input_grid[group_start:group_start + 4]

            for column_start in range(0, len(current_group[0]), 3):
                digit_pattern = []

                for row_index in range(len(current_group)):
                    digit_pattern.append(
                        current_group[row_index][column_start:column_start + 3]
                    )

                try:
                    full_final_word += pattern_dict[tuple(digit_pattern)]
                except KeyError:
                    full_final_word += "?"

            if group_start != len(input_grid) - 4:
                full_final_word += ","

        return full_final_word

    final_word = ""

    for column_start in range(0, len(input_grid[0]), 3):
        digit_pattern = []

        for row_index in range(len(input_grid)):
            digit_pattern.append(
                input_grid[row_index][column_start:column_start + 3]
            )

        try:
            final_word += pattern_dict[tuple(digit_pattern)]
        except KeyError:
            final_word += "?"

    return final_word