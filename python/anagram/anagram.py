def find_anagrams(word, candidates):
    """Return the candidate words that are anagrams of the target word.

    Parameters:
        word (str): The target word.
        candidates (list): A list of candidate words.

    Returns:
        list: The candidate words that are anagrams of the target word.
    """

    return [
        candidate for candidate in candidates
        if candidate.casefold() != word.casefold()
        and sorted(candidate.casefold()) == sorted(word.casefold())
    ]