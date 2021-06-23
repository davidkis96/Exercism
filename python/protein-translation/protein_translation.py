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
        if dictionary.get(codons) is not None:
            result.append(dictionary.get(codons))

    return result

def find_codon(codon):
    for kvp in dictionary:
        if type(kvp) is tuple:
            for item in kvp:
                if codon == item:
                    return kvp.
