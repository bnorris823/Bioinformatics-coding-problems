DNA = ""

from itertools import product

with open("DNA.txt")as file1:
    for line in file1:
        if line[0] != ">":
            DNA = DNA + line.strip()

def get_permutations(n):

    kmer_dict = {}
    letters = ['A', 'C', 'G', 'T']
    perm = list(product(letters, repeat=n))
    for p in perm:
        p = str(p)
        bad_chars = "()', "
        for char in bad_chars:
            p = p.replace(char, "")
        kmer_dict[p] = 0

    return(kmer_dict)

def count_kmers(DNA, n):
    kmer_dict = get_permutations(n)

    for k in range(len(DNA) - n + 1):
        kmer_dict[DNA[k:k+n]] += 1

    k_count = str(kmer_dict.values())[13:-2]
    k_count = k_count.replace(",", '')
    print(k_count)

count_kmers(DNA, 4)