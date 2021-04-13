"""
Write a function f that takes in a list of positive integers and returns True if it is quickly growing and False if it is not.

A list of integers [x1, x2, x3, ...] is quickly growing if all of the following are true:
- x2 >= 2*x1
- x3 >= 2*x2
- ...and so on.

The list will have at least two integers.
"""

def f(l):
	return all([2*a <= b for a, b in zip(l[:-1], l[1:])])

tests = [
    [1, 2],
    [10, 5],
    [2, 1],
    [80, 160],
    [10, 20, 30],
    [10, 20, 40],
    [1, 10, 100, 1000, 10000],
    [1, 10, 5, 1000, 10000],
    [1, 10, 100, 1000, 5],
    [5, 8, 100, 1000, 10000],
    [25, 50, 100, 199, 400],
    [1, 2, 3, 4],
    [2**n for n in range(20)]
    list(range(50)),
]
