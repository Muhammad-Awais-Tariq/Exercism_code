
import re

def count_words(sentence):
    """Takes a sentence and return the word count of all the words.

    Parameters:
        sentence (str): The given sentence.

    Returns:
        dict: The frequency of words in the sentence.
    """

    hash_map = {}
    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", sentence.lower())

    for word in words:
        if word in hash_map:
            hash_map[word] += 1
        else:
            hash_map[word] = 1

    return hash_map