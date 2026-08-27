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

    answer = []

    for item in range(len(items) - 1):
        answer.append(f"For want of a {items[item]} the {items[item + 1]} was lost.")

    if not qualifier:
        answer.append(f"And all for the want of a {items[0]}.")
    else:
        answer.append(f"And all for the want of a {qualifier} {items[0]}.")

    return answer