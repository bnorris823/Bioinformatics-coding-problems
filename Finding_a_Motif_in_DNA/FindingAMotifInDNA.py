dna = ""
sub = ""

def findMotif(a, s):
    loc = []
    
    for i in range(0, len(a)):
        if a[i:len(s) + i] == s:
            loc.append(i + 1)
    
    return loc
    
print(findMotif(dna, sub))  
