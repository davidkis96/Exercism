dictionary = {'AUG': 'Methionine',
              ('UUU', 'UUC'): 'Phenylalanine',
              ('UUA', 'UUG'): 'Leucine',
              ('UCU', 'UCC', 'UCA', 'UCG'): 'Serine',
              ('UAU', 'UAC'): 'Tyrosine',
              ('UGU', 'UGC'): 'Cysteine',
              'UGG': 'Tryptophan',
              ('UAA', 'UAG', 'UGA'): 'STOP'}


def proteins(strand):
    codon_list = [strand[i:i+3] for i in range(0, len(strand), 3)]
    result = []

    for codon in codon_list:
        if dictionary.get(codon) == "STOP":
            return result

        result.append(dictionary.get(codon))

    return result
