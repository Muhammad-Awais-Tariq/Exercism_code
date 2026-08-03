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
    pass


def length(list):
    pass


def map(function, list):
    pass


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    pass
