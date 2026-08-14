def rows(letter):
    """Draw a diamond pattern based on the given letter.

    Parameters:
        letter (str): The given letter.

    Returns:
        str: The diamond pattern.
    """

    for i in range(5):
        for j in range(5-i):
            print("*" , end=" ")
        for l in range(i):
            print("-" , end=" ")
        for m in range(i):
            print("-" , end=" ")
        for n in range(5-i):
            print("*" , end=" ")
        print()    

    for i in range(6):
        for l in range(i):
            print("*" , end=" ")
        for j in range(5-i):
            print("-" , end=" ")
        for m in range(5-i):
            print("-" , end=" ")
        for l in range(i):
            print("*" , end=" ")            
        print()
        
rows("a")