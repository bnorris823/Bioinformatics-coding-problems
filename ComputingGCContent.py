# Solution for http://rosalind.info/problems/gc/

from Bio import SeqIO
from Bio.SeqUtils import GC

maximum = 0.0
maxKey = ""

seqDict = SeqIO.to_dict(SeqIO.parse('test1.txt', 'fasta'))

for key in seqDict:
    if GC(seqDict[key].seq) > maximum:
        maximum = GC(seqDict[key].seq)
        maxKey = key

print(maxKey)
print(maximum)




