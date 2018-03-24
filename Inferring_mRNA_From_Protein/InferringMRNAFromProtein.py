def mRNAcombos(pseq):
    pcombo = {"I":3, "L":6, "V":4, "F":2, "M":1,
    "C":2, "A":4, "G":4, "P":4, "T":4, "S":6, 
    "Y":2, "W":1, "Q":2, "N":2, "H":2, "E":2, 
    "D":2, "K":2, "R":6, "STOP":3}
    seqcombo = 1
    
    for l in pseq:
        seqcombo *= pcombo[l]
        
    seqcombo *= 3
    return seqcombo % 1000000

pseq = ""

print(mRNAcombos(pseq))
