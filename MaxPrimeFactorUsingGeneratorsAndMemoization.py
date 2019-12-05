"""
Problem Statement: What is the largest prime factor of a given number?
Problem Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem

Unfortunately, this code could not pass some of the test cases due to timeout. 
"""

def arrfloor(arr, number):
    """Given an array in ascending order and a number, returns the index of the element which is just less than the number.
    Returns None when number is less than all the elements."""
    for i in range(len(arr)-1, -1, -1):
        if number >= arr[i]:
            return i
        
def memoize_generate_primes(function):
    """Stores cache for function."""
    memory = []
    prime = function()
    def inner(limit):
        """Generator that yields primes less than given limit. 
        It first checks whether the primes are already in the cache and then gets more primes if needed."""
        try:
            ind = arrfloor(memory, limit)
            yield from memory[:ind + 1]
            if arrfloor < (len(memory) - 1):
                return
                
        except TypeError:
            pass

        while True:
            new_prime = next(prime)
            memory.append(new_prime)
            if new_prime > limit:
                break
            yield new_prime
    return inner

@memoize_generate_primes
def generate_primes():
    """Generator that yields primes infinitely.
    This function is memoized, so whenever you call it, you're actually calling inner().
    """
    # Not original code. Taken from https://stackoverflow.com/a/568618/11679369
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

for _ in range(int(input())):
    number = int(input())
    try:
        ans = [i for i in generate_primes(number//2) if number % i == 0][-1] #[-1] will be the maximum factor.
    except IndexError:
        ans = number
    print(ans)
