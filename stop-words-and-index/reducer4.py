#!/usr/bin/env python
import sys, re, string

tuple_delimiter = "&&&"
last_word = None
found_at = ""

print("{")

for line in sys.stdin:

    line = line.strip()
    word, found = line.split("\t")
    word = word.strip()

    doc_title, line_num = found.split(tuple_delimiter)
    doc_title = doc_title.strip()
    line_num = line_num.strip()

    if not last_word:
        last_word = word

    if word == last_word:
        found_at += '["' + doc_title + '", "' + line_num + '"],'
    else:
        print('"' + last_word + '": ' + "[" + found_at[:-1] + "],")
        last_word = word
        found_at = '["' + doc_title + '", "' + line_num + '"],'

print('"' + word + '": ' + "[" + found_at[:-1] + "]")

print("}")
