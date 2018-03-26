def rComplement(seq):
    
    r = ""
    
    for x in seq:
        if x == 'A':
            r = 'T' + r
        elif x == 'C':
            r = 'G' + r
        elif x == 'G':
            r = 'C' + r
        elif x == 'T':
            r = 'A' + r
        else:
            print("not a nucleotide")
    
    return r
    
def rpalindrome(seq, n):
    if n % 2 != 0:
        print("n must be even")
        return -1
        
    pos_list = []    
        
    for i in range(0,(len(seq) - n + 1)):
        kmer = seq[i:i+n]
        kmer_r = rComplement(kmer)
        
        if kmer_r == kmer:
            pos_list.append(i + 1)
        
    return pos_list

seq = ""
pos_dict = {}
with open("input.fa")as fh:
    for line in fh:
        if line[0] != ">":
            seq += line.strip()
            
for x in range(4,13,2):
    p_list = rpalindrome(seq, x)
    if len(p_list) > 0:
        pos_dict[x] = p_list

for k in pos_dict.keys():
    for x in pos_dict[k]:
        print(x, k)
