#!/usr/bin/env python
# COSC 560 Software Systems
# Assignment 2 - MapReduce
# Part 4: SearchEngine
# Clayton Davis <cdavi151@vols.utk.edu>

from searchparser import SearchQueryParser
import json
import re
import os


#Inverted index search built on SearchQueryParser
#inspired by searchparser.py
class CdnwParser(SearchQueryParser):

    def __init__(self,index):
        self._methods = {
            'and': self.evaluateAnd,
            'or': self.evaluateOr,
            'not': self.evaluateNot,
            'parenthesis': self.evaluateParenthesis,
            'quotes': self.evaluateQuotes,
            'word': self.evaluateWord,
            'wordwildcard': self.evaluateWordWildcard,
            'keyword': self.evaluateKeyword,
            'between': self.evaluateBetween,
        }
        self._index = index
        self._parser = self.parser()

    def GetWord(self, word):
        if (self._index.has_key(word)):
            return set([tuple(each) for each in self._index[word]])
        else:
            return set()

    def GetWordWildcard(self, word):
        result = set()
        for item in self._index.keys():
            if word == item[0:len(word)]:
                result = result.union(set([tuple(each) for each in self._index[item]]))
        return result

    def GetBetween(self, min, max):
        result = set()
        for item in sorted(self._index.keys()):
            if min and item < min: continue
            if max and item > max: break
            result = result.union(set([tuple(each) for each in self._index[item]]))
        return result

    def GetQuotes(self, search_string, tmp_result):
        result = set()
        for item in tmp_result:
            print item
        return result

    def GetNot(self, not_set):
        print not_set
        all = set(self.docs.keys())
        return all.difference(not_set)


script_dir = os.path.dirname(__file__)

with open(os.path.join(script_dir,'..','stop-words-and-index','inverted_index.json')) as inverted_index_file:
    inverted_index = json.load(inverted_index_file)

with open(os.path.join(script_dir,'..','stop-words-and-index','stop-words.json')) as stop_words_file:
    stop_words = json.load(stop_words_file)

parser = CdnwParser(inverted_index)

#Executes a search against the index using a query string
def query_execute(query_str):
    query_str = query_str.lower()
    #for word in query_str.split(" "):
    #    if word in stop_words and word not in booleans:
    #        query_str = re.sub(word+'\s*', '', query_str)
    #print query_str
    results = parser.Parse(query_str)

    #Sort entries by title, then line number, then position
    for entry in sorted(
                    results,
                    key=lambda x: (x[0], int(x[1])) ):
        print(entry[0] + ' line ' + entry[1] + ' (' + entry[2] + ')'
                + ' position ' + entry[3])




if __name__ == "__main__":
    import sys
    print query_execute(" ".join(sys.argv[1:]))
