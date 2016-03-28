#!/usr/bin/env python
import sys, re, string, json, pprint

def doQuery():
    with open('inverted_index.json') as inverted_index_file:
        inverted_index = json.load(inverted_index_file)

    for word in sys.argv[1:]:
        if not word in inverted_index:
            continue
        for entry in sorted(inverted_index[word],key=lambda x: (x[0],int(x[1]))):
            print(word + ': ' + entry[0] + ' line ' + entry[1])





doQuery()
