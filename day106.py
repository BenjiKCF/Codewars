def DNA_strand(dna):
    new = []
    for ch in dna:
        if ch == 'A':
            new.append('T')
        elif ch == 'T':
            new.append('A')
        elif ch == 'C':
            new.append('G')
        elif ch == 'G':
            new.append('C')
        else:
            new.append('ch')
    return ''.join(new)


print DNA_strand("AAAA")#,"TTTT","String AAAA is")

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])
