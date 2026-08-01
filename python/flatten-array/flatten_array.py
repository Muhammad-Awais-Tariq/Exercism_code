def flatten(iterable):
    """Return a flattened list with all nested lists expanded.

    Parameters:
        iterable (list): The list to flatten.

    Returns:
        list: A flattened list.
    """

    flattened_list = []

    for item in iterable:

        if isinstance(item ,list):
            flattened_list.extend(flatten(item))
        elif item is not None:
            flattened_list.append(item)

    return flattened_list