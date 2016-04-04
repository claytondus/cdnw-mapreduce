#!/usr/bin/env python
import sys, re, string
stop_words_threshold = 50

for line in sys.stdin:
    line = line.strip()
    unpacked = line.split("\t")
    word = unpacked[0]
    doc_count = int(unpacked[1])
    if(doc_count > stop_words_threshold):
        print(word)


