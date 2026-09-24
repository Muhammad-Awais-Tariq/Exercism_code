def rectangles(strings):
    """Tell the number of rectangles based on the ascii characters.

    Parameters:
        strings(str): The ascii chracters based on which we will check.
    
    Returns:
        int: The number of the rectangles.
    """

    if len(strings) <= 1:
        return 0

    total_num = 0

    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if strings[i][j] == "+":
                for k in range(j + 1, len(strings[i])):
                    if strings[i][k] == "+":
                        for l in range(i + 1, len(strings)):
                            if strings[l][j] == "+" and strings[l][k] == "+":
                                valid = True

                                for o in range(j + 1, k):
                                    if strings[i][o] != "-":
                                        valid = False

                                for p in range(j + 1, k):
                                    if strings[l][p] != "-":
                                        valid = False

                                for q in range(i + 1, l):
                                    if strings[q][j] != "|":
                                        valid = False

                                    if strings[q][k] != "|":
                                        valid = False

                                if valid:
                                    total_num += 1

    return total_num