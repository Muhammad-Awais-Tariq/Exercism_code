def sum_of_multiples(limit, multiples):
    """Calculate the sum of all unique multiples below a given limit.

    Parameters:
        limit (int): The upper limit (exclusive).
        multiples (list): The numbers whose multiples are to be summed.

    Returns:
        int: The sum of all unique multiples below the limit.

    """
    total_multiples = set()

    for multiple in multiples:
        if multiple !=0:
            for devisor in range(limit):
                if devisor % multiple == 0 :
                    total_multiples.add(devisor)

    return sum(total_multiples)