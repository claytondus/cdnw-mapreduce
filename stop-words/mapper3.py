#!/usr/bin/env python
import sys, re, string

for line in sys.stdin:
    line = line.strip()
    unpacked = line.split("\t")
    word = unpacked[0]
    doc_count = int(unpacked[1])
    if(doc_count > 14):
        print(word)

# readin result words
# word 1
# words with # > x = stop words

# start inverted build

