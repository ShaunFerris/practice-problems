'''
Write a function that computes the nth fibonacci number
'''

'''
Solution one:
Use a dynamic programming approach with memoization.
To get the whole sequence to the nth number, return [0, 1 +
the values from the memoizer dict].
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

'''
Solution two:
Iterative approach that returns the whole sequence up to the
nth member. To just get the nth member, return out[-1.]
'''
def iterative_fib(nth):
    n1, n2, next_term = 1, 1, 0
    out = []
    for i in range(0, nth):
        out.append(n1)
        next_term = n1 + n2
        n1 = n2
        n2 = next_term
    return out

print(iterative_fib(10))