def find(search_list, value):
    """Return the index of a value in a sorted list using binary search.

    Parameters:
        search_list (list): The sorted list to search.
        value (int): The value to find.

    Returns:
        int: The index of the value in the list.

    Raises:
        ValueError: If the value is not found in the list.
    """

    left = 0
    right = len(search_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if value == search_list[middle]:
            return middle

        elif value < search_list[middle]:
            right = middle - 1

        elif value > search_list[middle] :
            left = middle + 1

    raise ValueError("value not in array")