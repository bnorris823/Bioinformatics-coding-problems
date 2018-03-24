def parse(file):
  f = open(file)
  title = ""
  seq = ""
  
  seqDict = {}
  
  for line in f:
    line = line.strip('\n')
    
    if line[0] == '>':
      line = line.strip('>')
      seqDict[title] = seq
      title = line
      seq = ""
    else:
      seq += line
  
  seqDict[title] = seq  
  seqDict.pop('', None)
  return seqDict
  
def seqMatrix(seqdict):
    sMatrix = []
    for key in seqdict:
        sMatrix.append(seqdict[key])
    return sMatrix
    
def nucMatrix(sMatrix):
    A = []
    C = []
    G = []
    T = []
    for i in range(len(sMatrix[0])):
        A.append(0)
        C.append(0)
        G.append(0)
        T.append(0)
    nMatrix = [A, C, G, T]
    return nMatrix
    
def profile(file):
    seqdict = parse(file)
    sMatrix = seqMatrix(seqdict)
    nMatrix = nucMatrix(sMatrix)
    
    for i in range(len(sMatrix)):
        for j in range(len(sMatrix[i])):
            if sMatrix[i][j] == 'A':
                nMatrix[0][j] += 1
            if sMatrix[i][j] == 'C':
                nMatrix[1][j] += 1
            if sMatrix[i][j] == 'G':
                nMatrix[2][j] += 1
            if sMatrix[i][j] == 'T':
                nMatrix[3][j] += 1  
    return nMatrix    
    
def consensus(nMatrix):
    cseq = ""
    for i in range(len(nMatrix[0])):
        numlist = []
        numlist.append(nMatrix[0][i])
        numlist.append(nMatrix[1][i])
        numlist.append(nMatrix[2][i])
        numlist.append(nMatrix[3][i])
        element = findMax(numlist)
        if (element == 0):
            cseq += 'A'
        if (element == 1):
            cseq += 'C'
        if (element == 2):
            cseq += 'G'
        if (element == 3):
            cseq += 'T'    
    return cseq   
        
        
        
        
def findMax(numlist):
    max1 = 0
    element = 0
    for n in range(len(numlist)):
        if (numlist[n] > max1):
            max1 = numlist[n]
            element = n
    return element        
    
nMatrix = profile("file1.py")
cseq = consensus(nMatrix)
    
def printResults(nMatrix, cseq):
    print(cseq)
    for i in range(len(nMatrix)):
        if i == 0:
            line = "A: "
            for n in nMatrix[i]:
                line += str(n) + " "
            print(line)
        if i == 1:
            line = "C: "
            for n in nMatrix[i]:
                line += str(n) + " "
            print(line)    
        if i == 2:
            line = "G: "
            for n in nMatrix[i]:
                line += str(n) + " "
            print(line)
        if i == 3:
            line = "T: "
            for n in nMatrix[i]:
                line += str(n) + " "
            print(line)

printResults(nMatrix, cseq)
