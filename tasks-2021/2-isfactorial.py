"""
Write a function f that takes in a positive integer n, and returns True if n is the factorial of some positive integer and False if it is not.

n will be at most 121645100408832000 = 20!.
"""

def f(n):
	i, r = 1, 1
	while True:
		if r == n:
			return True
		if r > n:
			return False
		i += 1
		r *= i

tests = [
    1,
    2,
    4,
    6,
    24,
    120,
    720,
    1040,
    19958400,
    479001600,
    1402373705728000,
    6402373705728000,
    121645100408831999,
    121645100408832000
]
