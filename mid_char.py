"""
    https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
    
    You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

    #Examples:

    Kata.getMiddle("test") should return "es"

    Kata.getMiddle("testing") should return "t"

    Kata.getMiddle("middle") should return "dd"

    Kata.getMiddle("A") should return "A"

"""

a = "abc"

# def get_middle(a):

#     ln = len(a)

#     mid = ln // 2

#     if ln % 2 == 0:
#         return a[mid-1:mid+1]
#     else:
#         return a[mid]


def get_middle(s):
   return s[(len(s)-1)//2:len(s)//2+1]

print(get_middle(a))