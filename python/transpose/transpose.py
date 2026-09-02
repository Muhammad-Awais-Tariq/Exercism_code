def transpose(text):
    """Takes the transpose of the given text.

    Parameters:
        text (str): The text we want to transpose.
    
    Return:
        str: The transposed text
    """

    if len(text) > 0:  

        words = text.split("\n")
        max_len = max(map(len , words))

        answer = [[" "] * len(words) for _ in range(max_len)]

        for row in range(len(words)):
            for column in range(max_len):
                if column < len(words[row]):
                    answer[column][row] = words[row][column]

        rows = []
        for row in answer:
            row_string = "".join(row)
            rows.append(row_string)

        return "\n".join(rows)

    return ""