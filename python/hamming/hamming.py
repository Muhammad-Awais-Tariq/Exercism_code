def distance(strand_a, strand_b):
    """Return the Hamming distance between two DNA strands.

    Parameters:
        strand_a (str): The first DNA strand.
        strand_b (str): The second DNA strand.

    Returns:
        int: The Hamming distance between the two DNA strands.

    The Hamming distance is the number of positions at which the
    corresponding nucleotides are different.
    """

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    hamming_distance = 0
    for letter in range(len(strand_a)):
        if strand_a[letter] != strand_b[letter]:
            hamming_distance +=1

    return hamming_distance