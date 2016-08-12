# Solution for http://rosalind.info/problems/rna/

DNA = "AAAAATTTTTGGGGGCCCC"
RNA = ""
for n in DNA:
    if n == 'T':
        RNA += 'U'
    elif n == 'A' or n == 'C' or n == 'G':
        RNA += n
    else:
        print("This is not a DNA sequence")
        break

print(RNA)
