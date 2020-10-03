"""
    https://www.codewars.com/kata/5a9a70cf5084d74ff90000f7/train/python

    You are given two positive integers a and b (a < b <= 20000). 
    Complete the function which returns a list of all those numbers in the interval [a, b) 
    whose digits are made up of prime numbers (2, 3, 5, 7) but which are not primes themselves.

    (2, 222) => [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75, 77]
    (2700, 3000) => [2722, 2723, 2725, 2727, 2732, 2733, 2735, 2737, 2752, 2755, 2757, 2772, 2773, 2775])
    
"""


def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def not_primes(num1,num2):
    out = []
    for item in range(num1,num2):
        if item > 10 and is_prime(item) == False and all(i in "2357" for i in str(item)):
            out.append(item)
    return out
