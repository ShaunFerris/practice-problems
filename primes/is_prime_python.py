'''
Implementation of the sieve of Erastothenes, a classical 
method for determining if a number is prime or not.
'''
from math import isqrt #this is just a floor sqrt function

'''
Solution one:
Basic seive, with the 6k +/- 1 optimization, meaning that 
all primes greater than 3 are of the form 6k ± 1, where k 
is any integer greater than 0. Other more complex 
implementations are much faster for larger n.
'''
def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

for i in range(1, 100):
    if is_prime(i):
        print(i)