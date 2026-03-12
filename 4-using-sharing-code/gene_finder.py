"""
Library for finding potential genes in a strand of DNA.
"""

import helpers


def get_complement(nucleotide):
    """
    Your docstring goes here.
    """
    pass


def get_reverse_complement(strand):
    """
    Your docstring goes here.
    """
    pass


def rest_of_orf(strand):
    """
    Your docstring goes here.
    """
    from textwrap import wrap
   #breaks strand into a list of 3 character long strings
    i=0
    final_strand = ""
    if len(strand)%3 == 0:
        chunk_strand = (wrap(strand, width=3))
    else:
        return 'Incorrect strand length'

    if strand[0] == 'ATG':
        while i < len(chunk_strand):
            if chunk_strand[i] == 'TAA':
                return final_strand
            if chunk_strand[i] == 'TAG':
                return final_strand
            if chunk_strand[i] == 'TGA':
                return final_strand
            else:
                final_strand = final_strand + (chunk_strand[i])
            i+=1



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
