#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:30:27 2018

@author: brandon
"""

import wget

def read_fasta(filename):
    dna = ''
    with open(filename)as file:
        for line in file:
            if line[0] != '>':
                dna = dna + line.strip()
    return dna

def make_prot_dict(prot_list):
    for p in prot_list:
        wget.download(f'http://www.uniprot.org/uniprot/{p}.fasta')
    
    
    prot_dict = {}
    for p in prot_list:
        prot_dict[p] = read_fasta(p + '.fasta')
    return prot_dict

def get_sites(seq):
    sites = []
    for i in range(0,len(seq)):
        if i + 4 < len(seq):
            k = seq[i:i+4]
            N = k[0] == 'N'
            P = k[1] != 'P' and k[3] != 'P'
            ST = k[2] == 'S' or k[2] == 'T'
            if N and P and ST:
                sites.append(i + 1)
    return sites

def print_output(site_dict):
    for k, v in site_dict.items():
        if v != []:
            print(k)
            print(' '.join(str(x) for x in v))

#main
prot_list = []
with open('data.txt')as data:
    for line in data:
        prot_list.append(line.strip())

prot_dict = make_prot_dict(prot_list)

site_dict = {}

for p in prot_dict:
    site_dict[p] = get_sites(prot_dict[p])
    
print_output(site_dict)

























