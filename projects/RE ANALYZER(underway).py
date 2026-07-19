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
    cut_positions = []
    for i in site_positions:
        cut_positions.append(i + offset_number)
    return cut_positions

print(dna_cut('TTTATGACGGTAGCAATAGCAATAGC', 'TGAC'))

sites = dna_cut('TTTATGACGGTAGCAATAGCAATAGC', 'TGAC')
print(offset_position(sites, 2))

cut_sequence=[]
for x in len(dna_cut(sequence)):
    if x == cut_positions:
        cut_sequence.append(dna_cut(x,len(restriction site+1)))
    else:
        pass
    
    