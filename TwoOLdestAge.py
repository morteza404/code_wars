"""
    https://www.codewars.com/kata/511f11d355fe575d2c000001/train/python

    The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].

    The order of the numbers passed in could be any order. The array will always include at least 2 items.

    For example:

    two_oldest_ages([1, 3, 10, 0]) # should return [3, 10]
"""

def two_oldest_ages(ages):
    out = []
    out.append(max(ages))
    ages.remove(max(ages))
    out.append(max(ages))
    return out[::-1]


print(two_oldest_ages([1, 3, 10, 0]))
print(two_oldest_ages([1, 5, 87, 45, 8, 8]))
print(two_oldest_ages([6, 5, 83, 5, 3, 18]))
print(two_oldest_ages([10, 1]))