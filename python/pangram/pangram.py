def is_pangram(sentence):
    """Check if the given sentence is a pangram.

    Parameters:
        sentence (str): The sentence to check.

    Returns:
        bool: True if the sentence is a pangram, otherwise False.
    """
    
    length_sentence = len(set(sentence.lower().replace(" " , "").removesuffix(".")))
    
    return length_sentence == 26
