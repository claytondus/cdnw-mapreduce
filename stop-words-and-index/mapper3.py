#!/usr/bin/env python
import sys, re, string

for line in sys.stdin:
    line = line.strip()
    unpacked = line.split("\t")
    word = unpacked[0]
    doc_count = int(unpacked[1])
    if(doc_count > 33):
        print(word)


