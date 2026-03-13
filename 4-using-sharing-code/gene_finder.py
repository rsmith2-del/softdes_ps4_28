"""
Library for finding potential genes in a strand of DNA.
"""

import helpers
from helpers import amino_acid
import random
from textwrap import wrap

COMPLIMENT_DICT = {"A": "T", "T": "A", "C": "G", "G": "C"}


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


def rest_of_orf(strand, include_start_codon=False):
    """
    Returns an orf, a strand of nucleotides from a start codon to an end codon.

    Args:
    strand- a string of nucleotides

    Returns:
    final_strand- a string of nucleotides that describes an orf


    """
    # breaks strand into a list of 3 character long strings
    i = 0
    final_strand = ""
    if len(strand) % 3 == 0:
        chunk_strand = wrap(strand, width=3)
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
            if include_start_codon and chunk_strand[i] == "ATG" and i > 0:
                return final_strand
            final_strand = final_strand + (chunk_strand[i])
            i += 1
        return ""
    return ""


def find_all_orfs_one_frame(strand):
    """
    Your docstring goes here.
    """
    orf_list = []
    while len(strand) > 0:
        next_orf_in_frame = rest_of_orf(strand, include_start_codon=True)
        next_index = len(rest_of_orf(strand, include_start_codon=False)) + 3
        orf_list.append(next_orf_in_frame)
        strand = strand[next_index:]
    return orf_list


def find_all_orfs(strand):
    """
    Your docstring goes here.
    """
    orfs_in_frame = find_all_orfs_one_frame(strand)
    orfs_shift_1 = strand[1:-2]
    chunk_shift_1 = wrap(orfs_shift_1, width=3)

    orfs_shift_2 = strand[2:-1]
    chunk_shift_2 = wrap(orfs_shift_2, width=3)

    i = 0
    shift_1_orfs_list = []
    shift_2_orfs_list = []

    while i < len(chunk_shift_1):
        if chunk_shift_1[i] == "ATG":

            shift_1_orfs_list.extend(find_all_orfs_one_frame(orfs_shift_1[((3 * i)) :]))
            break
        i += 1
    i = 0
    while i < len(chunk_shift_2):
        if chunk_shift_2[i] == "ATG":
            shift_2_orfs_list.extend(find_all_orfs_one_frame(orfs_shift_2[((3 * i)) :]))
            break
        i += 1
    all_in_out_orfs = orfs_in_frame + shift_1_orfs_list + shift_2_orfs_list

    final_all_orfs_list = []

    i = 0
    while i < len(all_in_out_orfs):
        if all_in_out_orfs[i] != "":
            final_all_orfs_list.append(all_in_out_orfs[i])
        i += 1

    return final_all_orfs_list


def find_all_orfs_both_strands(strand):
    """
    Your docstring goes here.
    """
    strand_1_orfs = find_all_orfs(strand)
    comp_orfs = find_all_orfs(get_reverse_complement(strand))

    orfs = []
    orfs.extend(strand_1_orfs)
    orfs.extend(comp_orfs)
    print(orfs)
    return orfs


def find_longest_orf(strand):
    """
    Your docstring goes here.
    """
    if len(find_all_orfs_both_strands(strand)) > 0:
        return max(find_all_orfs_both_strands(strand), key=len)
    return ""


def noncoding_orf_threshold(strand, num_trials):
    """
    Your docstring goes here.
    """
    i = 0
    min_length = 1000000000000000
    new_strand = list(strand)
    while i < num_trials:
        random.shuffle(new_strand)
        new_new_strand = "".join(new_strand)
        longest = find_longest_orf(new_new_strand)
        i += 1
        if longest != "":
            min_length = min(len(longest), min_length)
    return min_length


def encode_amino_acids(orf):
    """
    Your docstring goes here.
    """

    chunk_orf = wrap(orf, width=3)

    amino_acid_list = []
    i = 0
    while i < len(chunk_orf):
        if amino_acid(chunk_orf[i]) == "*":
            break
        if len(chunk_orf[i]) != 3:
            break
        amino_acid_list.append(amino_acid(chunk_orf[i]))
        i += 1
    return "".join(amino_acid_list)


def find_genes(path):
    """
    Your docstring goes here.
    """


# DON'T ADD ANYTHING ELSE TO THIS FILE. IF YOU DO, YOUR CODE MAY BE MARKED AS
# FAILING UNIT TESTS. IF YOU NEED TO TEST YOUR CODE, DO IT IN A JUPYTER
# NOTEBOOK.
