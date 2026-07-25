def to_rna(dna_strand):
    """Return the RNA sequence corresponding to the given DNA strand.

    Parameters:
        dna_strand (str): The DNA strand to transcribe.

    Returns:
        str: The RNA sequence corresponding to the given DNA strand.
    """

    dna_transcription = {
        "G" : "C" ,
        "C" : "G",
        "T" : "A" ,
        "A" : "U"
    }

    rna_seq = ""

    for char in dna_strand:
        rna_seq += dna_transcription[char]

    return rna_seq  