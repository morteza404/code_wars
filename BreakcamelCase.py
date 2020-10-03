"""
    https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

    Complete the solution so that the function will break up camel casing, using a space between words.

    Example
    solution("camelCasing")  ==  "camel Casing"
    solution("helloWorld") == "hello World"
    solution("camelCase") == "camel Case"
    solution("breakCamelCase") == "break Camel Case"
"""

def solution(s):
    for item in s:
        if item == item.upper():
            index = s.index(item)
    s = s[:index] + " " + s[index:]
    return s

print(solution("camelCasing"))



