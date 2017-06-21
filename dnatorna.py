"""
Converts DNA sequences to RNA.
"""

def rna(seq):
    """Convert a DNA sequence to RNA."""
    #Determine if the original sequence was uppercase
    seq_upper = seq.isupper()
    #Convert to lowercase
    seq = seq.lower()
    #swap out 't' for 'u'
    seq = seq.replace('t', 'u')
    #Return upper or lowe, depending on input
    if seq_upper:
        return seq.upper()
    else:
        return seq

def reverse_rna_complement(seq):
    """Convert a DNA sequence into its reverse comlement as RNA, changed doc string"""
    #Determine if the original sequence was uppercase
    seq_upper = seq.isupper()

    #reverse sequence
    seq= seq[::1]

    #convert to uppercase
    seq = seq.upper()

    #compute complement
    seq = seq.replace ('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace ('G', 'c')
    seq = seq.replace ('C', 'g')

    #return in appropriate case
    if seq_upper:
        return seq.upper()
    else:
        return seq
