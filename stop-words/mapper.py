#!/usr/bin/env python
import sys, re, string

last_line = ""
title = ""
for line in sys.stdin:
    line = line.strip()
    if(line!=""):
        if(title==""):
            if(line=="by William Shakespeare"):
                title = last_line
                line = title
            last_line = line
        
        if(title!=""):
            # strip punctuation
            line = re.sub('[\W_]+',' ',line.lower()).strip()
            unpacked = line.split(" ")
            for word in unpacked:
                word = word.strip()
                if(word != ""):
                    result = [title + ": " + word, "1"]
                    print("\t".join(result))

# readin result words
# word 1
# words with # > x = stop words

# start inverted build

