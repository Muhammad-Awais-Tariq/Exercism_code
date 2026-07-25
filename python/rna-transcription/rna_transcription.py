def to_rna(dna_strand):
    """Return the RNA sequence corresponding to the given DNA strand.

    Parameters:
        dna_strand (str): The DNA strand to transcribe.

    Returns:
        str: The RNA sequence corresponding to the given DNA strand.
    """

    if not dna_strand:
        return ""

    rna_seq = ""

    for char in dna_strand:
        if char == "G":
            rna_seq += "C"
        elif char == "C":
            rna_seq += "G"
        elif char == "T":
            rna_seq += "A"
        else:
            rna_seq += "U"      

    return rna_seq  