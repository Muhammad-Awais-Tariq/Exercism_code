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

    amino_acids = []

    for nucleotide in range(0 , len(strand) , 3):
        codon = strand[nucleotide : nucleotide + 3]

        if codon in codon_translation:
            if codon_translation[codon] == "STOP":
                return amino_acids

            amino_acids.append(codon_translation[codon])

    return amino_acids