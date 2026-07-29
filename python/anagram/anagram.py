def find_anagrams(word, candidates):
    """Return the candidate words that are anagrams of the target word.

    Parameters:
        word (str): The target word.
        candidates (list): A list of candidate words.

    Returns:
        list: The candidate words that are anagrams of the target word.
    """

    anagrams = []
    lower_word = word.lower()
    target = sorted(lower_word)

    for candidate in candidates:
        lower_candidate = candidate.lower()

        if lower_candidate != lower_word and target == sorted(lower_candidate):
            anagrams.append(candidate)

    return anagrams