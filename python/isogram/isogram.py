def is_isogram(phrase):
    """Check if the given phrase is an isogram.

    Parameters:
        phrase (str): The phrase to check.

    Returns:
        bool: True if the phrase is an isogram, otherwise False.
    """
    only_letters = [ltr for ltr in phrase.lower() if ltr.isalpha()]
    return len(set(only_letters)) == len(only_letters)