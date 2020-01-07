"""
Problem Statement:
Given lowercase string,
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Problem Link:
https://www.hackerrank.com/challenges/most-commons/problem
"""

# The editorial given to the problem has better solutions.

from collections import Counter, namedtuple
from functools import cmp_to_key

mynt = namedtuple('mynt', ['letter', 'count'])
str_nt = lambda nt: "{} {}".format(nt.letter, nt.count)

def cmp(one, two):
    """
    Accepts two mynts (named tuple object).
    Compares count (desc) if counts aren't equal.
    If they are, compares letter (asc).
    """
    if one.count == two.count:
        return (one.letter > two.letter) - (one.letter < two.letter)
    else:
        return -(one.count - two.count)

if __name__ == '__main__':
    string = input()

    ctr = Counter(string)
    mc = ctr.most_common()
    mc = [mynt(*i) for i in mc]

    wellsorted = sorted(mc, key = cmp_to_key(cmp))
    wellsorted = map(str_nt, wellsorted)
    wellsorted = list(wellsorted)
    print(*wellsorted[:3], sep = "\n")


