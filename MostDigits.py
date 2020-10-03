"""
    https://www.codewars.com/kata/58daa7617332e59593000006/train/python

    Find the number with the most digits.

    If two numbers in the argument array have the same number of digits, return the first one in the array.

    find_longest([1, 10, 100]) == 100
    find_longest([9000, 8, 800]) == 9000
    find_longest([8, 900, 500]) == 900
    find_longest([3, 40000, 100]) == 40000
    find_longest([1, 200, 100000]) == 100000
"""

def find_longest(arr):    
    ss = [len(str(i)) for i in arr]
    index = ss.index(max(ss))
    return arr[index]

print(find_longest([1, 200, 100000]))

