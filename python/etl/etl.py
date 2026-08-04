def transform(legacy_data):
    """Convert legacy letter-score data into a letter-to-score mapping.

    Parameters:
        legacy_data (dict): A dictionary mapping scores to lists of uppercase letters.

    Returns:
        dict: A dictionary mapping lowercase letters to their corresponding scores.
    """

    result = {}

    for key , letters in legacy_data.items():
        for letter in letters:
            result[letter.lower()] = key

    return result