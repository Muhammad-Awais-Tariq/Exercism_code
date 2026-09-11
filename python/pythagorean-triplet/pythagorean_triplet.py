def triplets_with_sum(number):
    """Return all Pythagorean triplets whose sum equals the given number.

    Parameters:
        number (int): The target sum of the Pythagorean triplets.

    Returns:
        list: A list of Pythagorean triplets whose elements sum to `number`.
    """

    triplets = []

    for first_side in range(1, number - 3):
        for second_side in range(first_side, number):
            third_side = number - first_side - second_side

            if third_side > second_side:
                if (first_side ** 2) + (second_side ** 2) == third_side ** 2:
                    triplets.append([first_side, second_side, third_side])

    return triplets