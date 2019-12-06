"""
Problem Statement: Find the largest palindrome made from the product of two 3-digit numbers which is less than N.
Problem Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem
"""
#Note: The largest palindrome which can be expressed as
# product of two three digit nos is 999*999 = 998001
# The smallest such palindrome would be 143*707 = 101101.

from math import ceil, sqrt

def generate_palindromes(start, stop, step = 1):
    """Generator to yield palindromes""" 
    for x in range(start, stop, step):
        if str(x) == str(x)[::-1]:
            yield x

def findfactors(p):
    """Given any number p, finds two three digit nos fac1 and fac2
    such that fac1*fac2 = p"""
    """Uses the equation (c-x)(c-y)-p=0 where c = ceil(sqrt p)."""
    c = ceil(sqrt(p))
    b = c*c - p
    numerator = lambda x: (b - c*x)
    denominator = lambda x: (x - c)
    
    for x in range(0, c - 100 + 1): # Note: At x = c - 100, fac1 = 100
        if numerator(x) % denominator(x) == 0:
            y = numerator(x)//denominator(x)
            fac1 = c - x
            fac2 = c + y
            
            if fac2 > 999: return None # factor exceeds three digits
            else: return fac1, fac2
            
    return None
        
if __name__ == "__main__":
    for _ in range(int(input())):
        upperlimit = int(input()) - 1
        for pal in generate_palindromes(upperlimit, 101100, -1):
            factors = findfactors(pal)
            if factors:
                print(pal)
                break
