def is_pangram(sentence):
    """Check if the given sentence is a pangram.

    Parameters:
        sentence (str): The sentence to check.

    Returns:
        bool: True if the sentence is a pangram, otherwise False.
    """
    unique_letters = set()

    for char in sentence.lower():
        if char.isalpha():
            unique_letters.add(char)
            
    return len(unique_letters) == 26