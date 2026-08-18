from string import punctuation


def abbreviate(words):
    """Return the acronym formed from the first letter of each word.

    Parameters:
        words (str): The words to create an acronym from.

    Returns:
        str: The acronym.
    """
    words = words.replace("-", " ")
    normalized_words = words.translate(words.maketrans("", "", punctuation))

    return "".join(word[0].upper() for word in normalized_words.split())