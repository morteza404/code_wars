"""
    Duplicate Encoder
    The goal of this exercise is to convert a string to a new string where each character in the new string is "(" 
    if that character appears only once in the original string, or ")" if that character appears more than once in the original string. 
    Ignore capitalization when determining if a character is a duplicate.

    Examples
        "din"      =>  "((("
        "recede"   =>  "()()()"
        "Success"  =>  ")())())"
        "(( @"     =>  "))(("
"""

import unittest
from collections import Counter

def duplicate_encode(word):
    output_string = ""
    frequency_per_char = Counter(word.lower())    
    for i in word:
        output_string += "(" if frequency_per_char[i] == 1 else ")"
    return output_string

# print(duplicate_encode("din"))
# print(duplicate_encode("recede"))
# print(duplicate_encode("Success"))
# print(duplicate_encode("(( @"))

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(duplicate_encode("din"),"(((")


    




