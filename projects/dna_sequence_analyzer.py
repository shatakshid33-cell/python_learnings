#my first project
dna=input("enter the dna sequence: ").upper()
print(dna)
print(f'Length of DNA sequence: {len(dna)}')
num=0
for i in dna:
    if i == "A":
        num = num+1
print(f'Number of Adenine bases: {num}')

ccount=0
for i in dna:
    if i =="C":
        ccount = ccount+1
print(f'Number of Cytosine bases: {ccount}')


gcount=0
for i in dna:
    if i =="G":
        gcount = gcount+1
print(f'Number of Guanine bases: {gcount}')

tcount=0
for i in dna:
    if i =="T":
        tcount = tcount+1
print(f'Number of Thymine bases: {tcount}')

gc_count=(gcount+ccount) / len(dna) * 100
print(f'GC content: {gc_count:.2f}%')

at_count=(acount+tcount) / len(dna) * 100
print(f'AT content: {at_count:.2f}%')