def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')

    return sum(a_part != b_part for a_part, b_part in zip(strand_a, strand_b))
