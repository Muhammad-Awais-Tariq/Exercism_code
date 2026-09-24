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
                for k in range(j + 1 , len(strings[i])):
                    if strings[i][k] == "+":
                        for o in range(j+1 , k ):
                            if strings[i][o] != "-":
                                pass
                        for l in range(i+1 , len(strings)):
                            if strings[l][j] == "+" and strings[l][k] == "+":
                                for p in range(j+1 , k):
                                    if strings[l][p] != "-":
                                        pass

                                for q in range(i+1 , l):
                                    if strings[q][j] != "|":
                                        pass

                                    if strings[q][k] != "|":
                                        pass
                                
                