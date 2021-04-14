"""
Write a function f that takes in a positive integer n. The output should be the integer result of interleaving the integers from 1 to n with the integers from n to 1.

For example, if the input is 4, the output should be 14233241.

Outputting either a string or an integer is acceptable.
"""

def f(n):
    return "".join(f"{a}{b}" for a, b in zip(range(1, n+1), range(n, 0, -1)))

tests = [1, 4, 10, 32, 100]

def checker(inp, tout, jout):
    return str(tout) == jout
