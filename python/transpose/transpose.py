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

        answer = [[None] * len(words) for _ in range(max_len)]

        for row in range(len(words)):
            for column in range(max_len):
                if column < len(words[row]):
                    answer[column][row] = words[row][column]
                elif any(len(words[later]) > column for later in range(row + 1, len(words))):
                    answer[column][row] = " "


        rows = []
        for row in answer:
            while row and row[-1] is None:
                row.pop()
            row_string = "".join(" " if c is None else c for c in row)
            rows.append(row_string)

        return "\n".join(rows)

    return ""