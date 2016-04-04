#!/usr/bin/env python
import sys, re, string, os

doc_start = "by William Shakespeare"

input_end = "End of the Project Gutenberg EBook"

skip_block_start = "<<"
skip_block_end = ">>"
skip_block = False
finished = False

last_line = ""
title = ""

file_name = ""

def fix_filename(file_name):
    fname = file_name
    if('/' in fname):
        parts = fname.split('/')
        fname = parts[-1:][0]
    return fname

for line in sys.stdin:
    if(file_name == ""):
        file_name = fix_filename(os.environ['mapreduce_map_input_file'])
    elif(file_name != fix_filename(os.environ['mapreduce_map_input_file'])):
        file_name = fix_filename(os.environ['mapreduce_map_input_file'])
        title = ""
        skip_block = False
        finished = False
    line = line.strip()
    if(line!=""):
        if(skip_block != True and finished != True):
            if(line[:len(skip_block_start)]==skip_block_start):
                skip_block = True
            elif(line[:len(input_end)]==input_end):
                finished = True
            else:
                if(line[:len(doc_start)]==doc_start):
                    title = "-" + last_line
                    line = title
                last_line = line
                
                if(title!="" or file_name!="pg100.txt"):
                    
                    line = re.sub('[\W_]+',' ',line.lower()).strip()
                    unpacked = line.split(" ")
                    for word in unpacked:
                        word = word.strip()
                        if(word != ""):
                            result = [file_name + title + ": " + word, "1"]
                            print("\t".join(result))
        
        elif(line[-(len(skip_block_end)):]==skip_block_end):
            skip_block = False

