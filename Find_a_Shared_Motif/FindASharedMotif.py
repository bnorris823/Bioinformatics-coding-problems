from difflib import SequenceMatcher
import time




def read_fasta(file):
    fasta_dict = {}

    with open(file)as data:
        header = ""
        seq = ""
        first = True
        for line in data:
            if line.startswith('>'):
                if first == False:
                    fasta_dict[header] = seq
                header = line.strip()
                seq = ""
                first = False
            else:
                seq += line.strip()

        fasta_dict[header] = seq

    return(fasta_dict)

#this function taken from: https://stackoverflow.com/questions/30046082/finding-a-shared-motif
def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr



start = time.time()
fasta_dict = read_fasta('data.fa')
string_list = []
for k in fasta_dict.keys():
    string_list.append(fasta_dict[k])
print(long_substr(string_list))
print(time.time() - start)









