def append(list1, list2):
    """Append the elements of the second list to the end of the first list.

    Parameters:
        list1 (list): The first list.
        list2 (list): The list whose elements will be appended.

    Returns:
        list: The first list with the elements of the second list appended.
    """

    return list1 + list2


def concat(lists):
    """Concatenate a list of lists into a single flat list.

    Parameters:
        lists (list): A list of lists.

    Returns:
        list: A single flattened list.
    """
    flattened_list = []

    for element in lists:
        flattened_list += element

    return flattened_list


def filter(function, list):
    """Return a list containing the elements for which the function returns True.

    Parameters:
        function (callable): The function used to test each element.
        list (list): The list to filter.

    Returns:
        list: A new list containing the elements that satisfy the function.
    """

    return [element for element in list if function(element)]


def length(list):
    """Return the number of elements in a list.

    Parameters:
        list (list): The list to measure.

    Returns:
        int: The number of elements in the list.
    """

    length_list = 0

    for element in list:
        length_list += 1

    return length_list    


def map(function, list):
    """Return a new list with the function applied to each element.

    Parameters:
        function (callable): The function to apply to each element.
        list (list): The list to transform.

    Returns:
        list: A new list containing the transformed elements.
    """

    return [function(element) for element in list]


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    pass
