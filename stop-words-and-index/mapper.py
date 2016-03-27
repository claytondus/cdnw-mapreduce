#!/usr/bin/env python
import sys, re, string

doc_start = "by William Shakespeare"

input_end = "End of the Project Gutenberg EBook"

skip_block_start = "<<"
skip_block_end = ">>"
skip_block = False
finished = False

last_line = ""
title = ""
for line in sys.stdin:
    line = line.strip()
    if(line!=""):
        if(skip_block != True and finished != True):
            if(line[:len(skip_block_start)]==skip_block_start):
                skip_block = True            
            elif(line[:len(input_end)]==input_end):
                finished = True
            else:
                if(line[:len(doc_start)]==doc_start):
                    title = last_line
                    line = title
                last_line = line
                
                if(title!=""):
                    
                    line = re.sub('[\W_]+',' ',line.lower()).strip()
                    unpacked = line.split(" ")
                    for word in unpacked:
                        word = word.strip()
                        if(word != ""):
                            result = [title + ": " + word, "1"]
                            print("\t".join(result))
        
        elif(line[-(len(skip_block_end)):]==skip_block_end):
            skip_block = False

