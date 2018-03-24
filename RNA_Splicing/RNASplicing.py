def parse(file):
  f = open(file)
  title = ""
  seq = ""
  
  seqlist = {}
  
  for line in f:
    line = line.strip('\n')
    
    if line[0] == '>':
      line = line.strip('>')
      seqlist[title] = seq
      title = line
      seq = ""
    else:
      seq += line
  
  seqlist[title] = seq  
  seqlist.pop('', None)
  return seqlist
  
#------------------------------------------------  

def translate(a):
    
    codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    
    prot = ""
    
    for i in range(0, len(a), 3):
        if codons[a[i:i+3]] != 'STOP':
            prot += codons[a[i:i+3]]
        
    return prot
    
#--------------------------------------------------------

def transcribe(a):
    rna = ""
    
    for x in a:
        if x == 'T':
            rna += 'U'
        else:
            rna += x
    
    return rna

#--------------------------------------------------------
def splice(dna, sub):
  for i in range(0, len(dna)):
    for s in sub:
      if dna[i:len(s) + i] == s:
        dna = dna.replace(dna[i:len(s) + i], "")
  
  return dna      
  
#--------------------------------------------------------
def spl_tsb_tlt(file):
  sdict = parse(file)
  
  seq = ""
  sub = []
  
  for key in sdict:
    if len(sdict[key]) > len(seq):
      seq = sdict[key]
      
  for key in sdict:
    if sdict[key] != seq:
      sub.append(sdict[key])
      
  
  dna = splice(seq, sub)
  rna = transcribe(dna)
  prot = translate(rna)
  
  return prot

print(spl_tsb_tlt('file1.py'))
