"""
https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

"""

a = 1234

# def count_bits(a):
#     out = ""
#     while a >= 1:
#         out += str(a%2)
#         a //= 2
#     # print(out[::-1])    
#     s = [i for i in out if i == "1"]
#     return len(s)

# print(count_bits(a))

"""
    clever solution

    bin() 
    count()

    def count_bits(a):
    return bin(a).count("1")

print(count_bits(a))
"""

