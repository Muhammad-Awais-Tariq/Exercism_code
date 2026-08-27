def proverb(*items, qualifier=None):
    """Generate a proverb from the given words.

    Parameters:
        items (str): The words used to construct the proverb.
        qualifier (str, optional): An optional word added to the final line.

    Returns:
        str: The generated proverb.
    """

    if not items:
        return []