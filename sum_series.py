"""
    https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

    Task:
    Your task is to write a function which returns the sum of following series upto nth term(parameter).    

    Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

    Test.assert_equals(series_sum(1), "1.00")
    Test.assert_equals(series_sum(2), "1.25")
    Test.assert_equals(series_sum(3), "1.39")

"""

def series_sum(n):
    total = 0
    for i in range(1,n +1):
        total += 1 / (3 * i - 2)
    return "%.2f" % total

print(series_sum(3))