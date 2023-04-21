'''
Write a function to find the lowest common multiple for
all numbers in a range between the two numbers provided in
an array.
'''

from functools import reduce

TEST_ARRAY = [1, 5]

def lcm(arr):
    min, max = sorted(arr)
    arr_range = [i for i in range(min, max + 1)]
    limit = reduce(lambda product, current: product * current, arr_range)
    for i in range(max, limit + 1, max):
        if all(i % value == 0 for value in arr_range):
            return i

print(lcm(TEST_ARRAY))