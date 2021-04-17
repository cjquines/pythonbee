"""
Write a function f that takes in a positive integer n, and returns the largest banknote number less than or equal to n.

The banknote numbers are 1, 2, or 5 times a power of 10. They begin 1, 2, 5, 10, 20, 50, 100, 200, 500.

The input will be at most 1000000000000000 = 10^15.
"""

# https://codegolf.stackexchange.com/questions/210671/find-the-largest-banknote

def f(n):
    return 10*f(n//10) if n >= 10 else max(c for c in [1, 2, 5] if c <= n)

tests = [
    1,
    2,
    3,
    5,
    10,
    99,
    100,
    729871,
    3789345345234,
    999999999999999,
    1000000000000000
]
