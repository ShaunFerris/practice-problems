'''
Write a function that computes the fibonnaci number at a given index i
along the fibonacci sequence. Use a dynamic programming approach with memoization.
'''

MEMOIZER = {}

def fib(i):
    key = '' + str(i)
    if key in MEMOIZER:
        return MEMOIZER[key]
    if i == 0:
        return 0
    elif i == 1:
        return 1
    
    result = fib(i - 1) + fib(i - 2)
    MEMOIZER[key] = result
    return result

print(fib(10))