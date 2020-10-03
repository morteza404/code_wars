"""
    Sum Array
    Write a method sum (sum_array in python, sumarray in julia, SumArray in C#) that takes an array of numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers can also be negative. If the array does not contain any numbers then you should return 0.

    Examples
    print sum_array([1 2 3])
    > 6
    print sum_array([])
    > 0
"""

def sum_array(a):
    total = 0
    for i in a:
        total += i
    return total