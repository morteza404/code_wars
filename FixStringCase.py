"""
https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

"""

def solve(s):    

    lower_lst = []

    upper_lst = []

    for item in s:
        if item == item.lower():
            lower_lst.append(item)
        else:
            upper_lst.append(item)    

    lower_indices = [s.index(i) for i in s if i == i.lower()]

    upper_indices = [s.index(i) for i in s if i == i.upper()]

    if len(lower_lst) >= len(upper_lst):
        for item in upper_indices:
            s = s[:item] + s[item].lower() + s[item+1:]
    else:
        for item in lower_indices:
            s = s[:item] + s[item].upper() + s[item+1:]   

    return s

print(solve("CoDE"))
