"""
5 kyu

"""


import math

def zeros(n):
    s = str(math.factorial(n))
    tot = 0
    while s.endswith("0"):
        tot += 1
        s=s[:-1]
    return tot

print(zeros(30))

"""
def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0

"""