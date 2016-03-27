#!/usr/bin/env python
import sys, re, string

for line in sys.stdin:
    line = line.strip()
    unpacked = line.split(": ")
    tmp_split = unpacked[1].split("\t")
    word = tmp_split[0]
    result = [word, "1"]
    print("\t".join(result))

# readin result words
# word 1
# words with # > x = stop words

# start inverted build

