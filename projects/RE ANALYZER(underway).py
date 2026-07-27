def dna_cut(sequence, restriction_site):
    """Find all (including overlapping) positions of restriction_site in sequence."""
    start = 0
    site_positions = []
    while True:
        cut_position = sequence.find(restriction_site, start)
        if cut_position == -1:
            break
        site_positions.append(cut_position)
        start = cut_position + 1
    return site_positions


def offset_position(site_positions, offset_number):
    """Shift each site position by a fixed offset (where the enzyme actually cuts)."""
    cutting_positions = []
    for i in site_positions:
        cutting_positions.append(i + offset_number)
    return cutting_positions


def cut_sequence(sequence, cutting_positions):
    """Slice sequence into fragments at the given cutting positions."""
    fragments = []
    prev = 0
    for pos in cutting_positions:
        fragments.append(sequence[prev:pos])
        prev = pos
    fragments.append(sequence[prev:])  # last piece
    return fragments


def restriction_digest(sequence, restriction_site, offset_number=0):
    """Convenience wrapper: run the full find -> offset -> cut pipeline."""
    site_positions = dna_cut(sequence, restriction_site)
    cutting_positions = offset_position(site_positions, offset_number)
    return cut_sequence(sequence, cutting_positions)


if __name__ == "__main__":
    seq = 'tttaaaggcctggatgcgcggtagatgcggttaagccgta'
    site = 'tag'

    positions = dna_cut(seq, site)
    print("site positions:", positions)

    offsets = offset_position(positions, 1)
    print("offset positions:", offsets)

    fragments = cut_sequence(seq, offsets)
    print("fragments:", fragments)

    # or in one call:
    print("digest():", restriction_digest(seq, site, offset_number=1))