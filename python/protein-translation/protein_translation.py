dictionary = {'AUG': 'Methionine',
              ('UUU', 'UUC'): 'Phenylalanine',
              ('UUA', 'UUG'): 'Leucine',
              ('UCU', 'UCC', 'UCA', 'UCG'): 'Serine',
              ('UAU', 'UAC'): 'Tyrosine',
              ('UGU', 'UGC'): 'Cysteine',
              'UGG': 'Tryptophan',
              ('UAA', 'UAG', 'UGA'): 'STOP'}


def proteins(strand):
    codon_group = [strand[i:i+3] for i in range(0, len(strand), 3)]
    result = []

    for codons in codon_group:
        codon = find_codon(codons)
        if codon == 'STOP':
            return result
        else:
            result.append(codon)

    return result


def find_codon(codon):
    for k in dictionary.keys():
        if type(k) is str:
            if codon == k:
                return dictionary[k]
        if type(k) is tuple:
            if codon in k:
                return dictionary[k]
