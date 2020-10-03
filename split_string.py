"""
    https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
    
    Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

    Examples:

    solution('abc') # should return ['ab', 'c_']
    solution('abcdef') # should return ['ab', 'cd', 'ef']

"""

a = "abc"

def solution(a):
    out = [a[i:i+2] for i in range(0 , len(a) , 2)]
    if len(out[-1]) == 1:    
        out[-1] = out[-1] + "_"
    return out

print(solution(a))
