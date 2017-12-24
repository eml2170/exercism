def to_rna(dna_strand):
    if len(set(dna_strand) - set(['G','C','T','A'])) > 0:
               raise ValueError('invalid input')
    return dna_strand.replace('G','c').replace('C','G').replace('c','C') \
.replace('A','U').replace('T','A')
