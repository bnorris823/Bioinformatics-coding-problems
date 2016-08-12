# Solution for http://rosalind.info/problems/revc/

DNA = "AAAACCCGGT"
complement = ""

for n in DNA:
    if n == 'A':
        complement += 'T'
    elif n == 'T':
        complement += 'A'
    elif n == 'C':
        complement += 'G'
    elif n == 'G':
        complement += 'C'
    else:
        print("This is not a DNA sequence")
        break
complement = complement[::-1]
print(complement)
