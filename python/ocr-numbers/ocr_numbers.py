def convert(input_grid):
    """Converts the input grid into the numbers.

    Parameters:
        input_grid (list) : The given chracter.
    
    Returns:
        int: The recognized digit.
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
        for i in range(0 , len(input_grid) , 4):
            current_word = input_grid[i:i+4]
            for j in range(0 , len(current_word[0]) , 3):
                temp_word = []
                for k in range(len(current_word)):
                    temp_word.append(current_word[k][j:j+3])            
                try:
                    full_final_word += f"{pattern_dict[tuple(temp_word)]}"
                except KeyError:
                    full_final_word += "?"

            if i != len(input_grid) - 4:
                full_final_word += ","

        return full_final_word
    
    else:
        final_word = ""
        for j in range(0 , len(input_grid[0]) , 3):
            current_word = []
            for i in range(len(input_grid)):
                current_word.append(input_grid[i][j:j+3])

            try:
                final_word += pattern_dict[tuple(current_word)]
            except KeyError:
                final_word += "?"

        return final_word