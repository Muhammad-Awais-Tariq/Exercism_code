def recite(start, take=1):
    """Recite the verses based on the start index.

    Parameters:
        start (int): The start index to start the verse from.
        take (int): How many verses we want.
    """

    number_words = {
        0: "no",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
    }

    verses = []
    current = 0
    for i in range(start , 0 , -1):
        bottle = "bottle" if i == 1 else "bottles"
        next_bottle = "bottle" if i - 1 == 1 else "bottles"
        verses.extend([
            f"{number_words[i]} green {bottle} hanging on the wall,",
            f"{number_words[i]} green {bottle} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {number_words[i - 1].lower()} green {next_bottle} hanging on the wall.",
        ])
        

        current += 1

        if current == take:
            break

        if i != 1:
            verses.append("")        

    return verses
