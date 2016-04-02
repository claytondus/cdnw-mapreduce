#!/usr/bin/env python
import sys, re, string, json


def add_line_to_index(this_line):
    #strip punctuation
    cleaned = re.sub('[\W_]+',' ',this_line.lower()).strip()
    for match in re.finditer(r'\S+', cleaned):
        position, word = match.start(), match.group()
        word = word.strip()
        if word != "" and word not in stop_words:
            result = [word, title + tuple_delimiter + str(line_count) + '","' + str(real_line) + '","' + str(position) ]
            print("\t".join(result))


jstop = None
with open("stop-words.json","r") as f:
    jstop = json.load(f)
stop_words = set(jstop)

# easiest delimiter but is 5th line of each doc with date, blank, title, blank preceeding
doc_start = "by William Shakespeare"

input_end = "End of the Project Gutenberg EBook"

skip_block_start = "<<"
skip_block_end = ">>"
skip_block = False
finished = False

tuple_delimiter = "&&&"

last_line = ""
last_line2 = ""
title = ""
line_count = 0
real_line = 0

for line in sys.stdin:
    line = line.strip()
    line_count += 1
    real_line += 1
    if(line!=""):
        if(skip_block != True and finished != True):
            if(line[:len(skip_block_start)]==skip_block_start):
                skip_block = True
            elif(line[:len(input_end)]==input_end):
                finished = True
            else:
                if(line[:len(doc_start)]==doc_start):
                    title = last_line
                    year = last_line2
                    add_line_to_index(year)
                    add_line_to_index(title)
                    line_count = 5
                else:
                    if(title!=""):
                        add_line_to_index(line)

                last_line2 = last_line
                last_line = line


        elif(line[-(len(skip_block_end)):]==skip_block_end):
            skip_block = False
