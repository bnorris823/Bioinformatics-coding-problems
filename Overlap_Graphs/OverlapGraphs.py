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

seqDict = parse('file1.py')

def graphPairs(seqDict, k):
    plist = []
    for key in seqDict:
        suf = seqDict[key][-k:]
        for l in seqDict:
            pair = [key]
            pre = seqDict[l][:k]
            if ((suf == pre) & (key != l)):
                pair.append(l)
            if(len(pair) > 1):    
                plist.append(pair)
    return plist    

def printPairs(pairs):
    for i in range(len(pairs)):
        print(" ".join(pairs[i]))

pairs = graphPairs(seqDict, 3)
printPairs(pairs)
