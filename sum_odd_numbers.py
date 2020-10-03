"""
    https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
    
    Given the triangle of consecutive odd numbers:

                 1
              3     5
           7     9    11
       13    15    17    19
    21    23    25    27    29
    ...
    Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

    row_sum_odd_numbers(1); # 1
    row_sum_odd_numbers(2); # 3 + 5 = 8

"""

def sum_odd(n):

    total = 0

    a = [i for i in range(1,n ** 2 + n,2)]

    a = a[-1:-(n+1):-1]

    for i in a:
        total += i

    return total

print(sum_odd(2))
