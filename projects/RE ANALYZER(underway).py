def dna_cut(sequence, restriction_site):
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
    cutting_positions = []
    for i in site_positions:
        cutting_positions.append(i + offset_number)
    return cutting_positions


def cut_sequence(sequence, cutting_positions):
    fragments = []
    prev = 0
    for pos in cutting_positions:
        fragments.append(sequence[prev:pos])
        prev = pos
    fragments.append(sequence[prev:])  # last piece
    return fragments
print fragments


print(dna_cut('tttaaaggcctggatgcgcggtagatgcggttaagccgta','tag'))
