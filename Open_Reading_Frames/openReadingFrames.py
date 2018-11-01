#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:58:06 2018

@author: brandon
"""
import re

def read_data(filename):
    dna = ''
    with open(filename) as file:
        for line in file:
            if line[0] != '>':
                dna = dna + line.strip()
    return dna

def reverse_complement(DNA):
    '''Takes a DNA sequence and returns its reverse complement.'''
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
    return complement[::-1]

def DNA2RNA(DNA):
    RNA = ""
    for n in DNA:
        if n == 'T':
            RNA += 'U'
        elif n == 'A' or n == 'C' or n == 'G':
            RNA += n
        else:
            print("This is not a DNA sequence")
            
    return RNA

def get_codons(RNA):
    codon_list_all = []
    for n in [0, 1, 2]:
        codon_list = []
        for i in range(n,len(RNA), 3):
            c = RNA[i:i+3]
            if len(c) >= 3:
                codon_list.append(c)
        codon_list_all.append(codon_list)
    return codon_list_all
        
def translate(codon_lists):
    prot_list = []
    for i in codon_lists:
        prot = ''
        for c in i:
            prot = prot + codons[c]
        prot_list.append(prot)
            
    return prot_list
                
def parse_prot(prot_list):
    
    ind = []
    for p in prot_list:
        m_list = [m.start() for m in re.finditer('M', p)]
        
        if len(m_list) > 0:
            m_list2 = []
            for m in m_list:
                pre = p[m:]
                if 'STOP' in pre:
                    post = pre[:pre.find('STOP')]
                    if len(post) > 0:
                        m_list2.append(post)
            if len(m_list2) > 0:    
                ind.append(m_list2)
                
    final = []
    for l in ind:
        final = final + l
    return list(set(final))

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


dna = read_data('data.fa')
rDNA = reverse_complement(dna)
RNA = DNA2RNA(dna)
rRNA = DNA2RNA(rDNA)

prot_list = translate(get_codons(RNA))
prot_list = prot_list + translate(get_codons(rRNA))

prot_list = parse_prot(prot_list)

for p in prot_list:
    print(p)
        
































