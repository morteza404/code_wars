"""
https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

Count characters in your string

6 kyu

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

"""


from collections import Counter

def count(s):
    return dict(Counter(s))

print(count("aba"))