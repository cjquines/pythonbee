"""
Write a function f that takes in two positive integers m and n. It should return the number of ordered pairs (a, b) of positive integers such that a <= m, b <= n, and a + b is divisible by 5.

The positive integers in the input will be at most 100.
"""

# https://codegolf.stackexchange.com/questions/205294/pairs-with-sum-divisible-by-5

def f(m, n):
    return len([(a, b) for a in range(1, m+1) for b in range(1, n+1) if (a + b) % 5 == 0])

tests = [
    (1, 1),
    (1, 100),
    (6, 12),
    (11, 14),
    (29, 29),
    (100, 100),
    (31, 43)
]
