def proteins(strand):
    """Convert an RNA strand into a list of proteins.

    Parameters:
        strand (str): The RNA sequence.

    Returns:
        list: A list of amino acids.
    """

    codon_translation = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }

    Amino_acids = []

    for nucleotide in range(0 , len(strand) , 3):
        condon = strand[nucleotide : nucleotide + 3]

        if condon in codon_translation.keys():
            if codon_translation[condon] == "STOP":
                return Amino_acids

            Amino_acids.append(codon_translation[condon])

    return Amino_acids