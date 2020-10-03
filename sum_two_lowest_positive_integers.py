a = [25, 42, 12, 18, 22]


def sum_two_smallest_numbers(numbers):

    min1 = min(numbers)

    ix = numbers.index(min1)

    del numbers[ix]

    min2 = min(numbers)

    return min1 + min2

print(sum_two_smallest_numbers(a))
