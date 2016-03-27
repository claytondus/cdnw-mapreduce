#!/usr/bin/env python
import sys, re, string

last_word = None
word = ""

print("[")
for line in sys.stdin:

    line = line.strip()
    word = line

    if not last_word:
        last_word = word

    if word != last_word:
        print('"' + word + '",')
        last_word = word

print('"' + word + '"')
print("]")
