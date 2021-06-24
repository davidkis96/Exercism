def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Invalid input! Cannot compare strands of different lengths")

    differences = 0

    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            differences += 1

    return differences
