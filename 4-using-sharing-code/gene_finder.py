"""
Library for finding potential genes in a strand of DNA.
"""

import helpers

COMPLIMENT_DICT = {"A": "T", "T": "A", "C": "G", "G": "A"}


def get_complement(nucleotide):
    """
    Returns the complimentary nucleotide for a given nucleotide 'A', 'T', 'C', or 'G'

    Args:
        nucleotide: a single character string representing one of the four nucleotides

    Returns:
        the compliment of nucleotide
    """
    return COMPLIMENT_DICT[nucleotide]


def get_reverse_complement(strand):
    """
    Returns the reversed compliment of a given strand of nucleotides

    Args:
        strand: a string representing a strand of DNA

    Returns:
        the reversed compliment of the given strand of DNA
    """
    reverse_compliment = ""
    for nucleotide in strand:
        reverse_compliment = reverse_compliment + get_complement(nucleotide)
    return reverse_compliment[::-1]


def rest_of_orf(strand):
    """
    Returns an orf, a strand of nucleotides from a start codon to an end codon.

    Args:
    strand- a string of nucleotides

    Returns:
    final_strand- a string of nucleotides that describes an orf


    """
    from textwrap import wrap

    # breaks strand into a list of 3 character long strings
    i = 0
    final_strand = ""
    if len(strand) % 3 == 0:
        chunk_strand = wrap(strand, width=3)
        print(chunk_strand)
        print(chunk_strand[0])
    else:
        return ""

    if chunk_strand[0] == "ATG":
        while i < len(chunk_strand):
            if chunk_strand[i] == "TAA":
                return final_strand
            if chunk_strand[i] == "TAG":
                return final_strand
            if chunk_strand[i] == "TGA":
                return final_strand
            else:
                final_strand = final_strand + (chunk_strand[i])
            i += 1
        return ""
    return ""


def find_all_orfs_one_frame(strand):
    """
    Your docstring goes here.
    """
    pass


def find_all_orfs(strand):
    """
    Your docstring goes here.
    """
    pass


def find_all_orfs_both_strands(strand):
    """
    Your docstring goes here.
    """
    pass


def find_longest_orf(strand):
    """
    Your docstring goes here.
    """
    pass


def noncoding_orf_threshold(strand, num_trials):
    """
    Your docstring goes here.
    """
    pass


def encode_amino_acids(orf):
    """
    Your docstring goes here.
    """
    pass


def find_genes(path):
    """
    Your docstring goes here.
    """
    pass


# DON'T ADD ANYTHING ELSE TO THIS FILE. IF YOU DO, YOUR CODE MAY BE MARKED AS
# FAILING UNIT TESTS. IF YOU NEED TO TEST YOUR CODE, DO IT IN A JUPYTER
# NOTEBOOK.
