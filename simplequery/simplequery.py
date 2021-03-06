#!/usr/bin/env python
# COSC 560 Software Systems
# Assignment 2 - MapReduce
# Part 3: Query
# Clayton Davis <cdavi151@vols.utk.edu>


import sys, json, os

script_dir = os.path.dirname(__file__)

def doQuery():
    with open(os.path.join(script_dir,'..','stop-words-and-index','inverted_index.json')) as inverted_index_file:
        inverted_index = json.load(inverted_index_file)

    #Loop through each query word and output matching index entries
    for word in sys.argv[1:]:
        if not word in inverted_index:
            continue
        #Sort entries by title, then line number, then position
        for entry in sorted(inverted_index[word],key=lambda x: (x[0], int(x[1]), int(x[3]))):
            print(word + ': ' + entry[0] + ' line ' + entry[1] + ' position ' + entry[3])





doQuery()
