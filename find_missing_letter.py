"""
    https://www.codewars.com/kata/5839edaa6754d6fec10000a2/solutions/python

    6 kyu
    
    ["a","b","c","d","f"] -> "e"
    ["O","Q","R","S"] -> "P"
"""

import string

def find_missing_letter(l):
    ix = string.ascii_letters.index(l[0])
    return list(set(string.ascii_letters[ix:ix+len(l)+1]) - set(l))[0]

print(find_missing_letter(["a","b","c","d","f"]))
