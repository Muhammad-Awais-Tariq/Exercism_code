def rows(letter):
    """Draw a diamond pattern based on the given letter.

    Parameters:
        letter (str): The given letter.

    Returns:
        str: The diamond pattern.
    """

    letter_position = ord(letter) - 65

    for i in range(letter_position+1):
        for j in range(letter_position-i):
            print(" " , end=" ")
        print(chr (i + 65) , end=" ")
        print()

    # for i in range(5):
    #     for j in range(5-i):
    #         print("*" , end=" ")
    #     for l in range(i):
    #         print("-" , end=" ")
    #     for m in range(i):
    #         print("-" , end=" ")
    #     for n in range(5-i):
    #         print("*" , end=" ")
    #     print()    

    # for i in range(6):
    #     for l in range(i):
    #         print("*" , end=" ")
    #     for j in range(5-i):
    #         print("-" , end=" ")
    #     for m in range(5-i):
    #         print("-" , end=" ")
    #     for l in range(i):
    #         print("*" , end=" ")            
    #     print()
rows("E")