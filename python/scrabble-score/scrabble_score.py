def score(word: str) -> int:
    """Takes a word and return the Scrabble score.

    Parameters:
        word (str): The word we want score of.
    
    Returns:
        int: The scrabble score.
    """

    letter_values = {
        ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
        ("D", "G"): 2,
        ("B", "C", "M", "P"): 3,
        ("F", "H", "V", "W", "Y"): 4,
        ("K",): 5,
        ("J", "X"): 8,
        ("Q", "Z"): 10,
    }