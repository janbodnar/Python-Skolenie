#!/usr/bin/python

# compare.py

import csv

rows_1 = {}
rows_2 = {}

with open('data1.csv', 'r') as f1, open('data2.csv', 'r') as f2:

    reader = csv.reader(f1, delimiter=",")
    
    for row in reader:
        rows_1[int(row[0])] = row[1:]
        
    reader = csv.reader(f2, delimiter=",")
    
    for row in reader:
        rows_2[int(row[0])] = row[1:]
        
    
    not_match_idxs = set(rows_1.keys()) - set(rows_2.keys())
    
    print ("Not matching indexes:", end=" ")
    
    for idx in not_match_idxs:
        print(idx, end=" ")
        
    match_idxs = set(rows_1.keys()) & set(rows_2.keys())
    
    print()
    
    print ("Matching indexes:", end=" ")
    
    for idx in match_idxs:
        print(idx, end=" ")
        
    sorted_matching_keys = sorted(match_idxs)
    
    print()
    
    diffs = []
    
    for idx in sorted_matching_keys:
        if ((rows_1[idx] != rows_2[idx])):
           diffs.append(idx)
    
    print ("Differences:", end=" ")
    print (diffs)
        

