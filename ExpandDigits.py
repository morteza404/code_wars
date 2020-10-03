"""
    https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

    Write Number in Expanded Form
    You will be given a number and you will need to return it as a string in Expanded Form. For example:

    expanded_form(12) # Should return '10 + 2'
    expanded_form(42) # Should return '40 + 2'
    expanded_form(70304) # Should return '70000 + 300 + 4'
    NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
    number = str(num)
    total = ""
    ln = len(number)
    for i in range(ln):       
        s = number[i] + "0" * (ln -1)  
        if all(v == "0" for v in s):
            ln -= 1
            continue
        total +=  s + " + "               
        ln -= 1
    return total.rstrip(" + ")

print(expanded_form(42))

"""
enumerate()

def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
"""






