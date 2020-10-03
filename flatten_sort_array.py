"""
    https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python
    
    Challenge:

    Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

    Example:

    Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

"""

"""
    https://www.w3schools.com/python/ref_func_sorted.asp#:~:text=The%20sorted()%20function%20returns,string%20values%20AND%20numeric%20values.

    Python sorted() Function

    The sorted() function returns a sorted list of the specified iterable object.

    You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

    Note: You cannot sort a list that contains BOTH string values AND numeric values.

"""

"""
    https://www.geeksforgeeks.org/python-itertools-chain/
    Python – Itertools.chain()
"""

a = [[3, 2, 1], [7, 9, 8], [6, 4, 5]]


def flatten_and_sort(a):
    for i in a:
        i.sort()
    b = [j for i in a for j in i]
    b.sort()
    return b

print(flatten_and_sort(a))

"""
from itertools import chain
def flatten_and_sort(array):
    return sorted((chain(*array)))

"""

"""
def flatten_and_sort(array):
    return sorted([j for i in array for j in i])

"""




