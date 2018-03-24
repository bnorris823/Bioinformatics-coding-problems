dna1 = "GAGCCTACTAACGGGAT"
dna2 = "CATCGTAATGACGGCCT"
mut_count = 0

if len(dna1) == len(dna2):
    for i in range(0, len(dna1)):
        if dna1[i] != dna2[i]:
            mut_count += 1
            
print(mut_count)
