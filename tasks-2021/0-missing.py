"""
Write a function f that takes in the sorted list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], except one of the integers is missing. Return the missing integer.
"""

def f(a):
	return 45 - sum(a)

tests = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 9],
    [0, 1, 2, 3, 4, 5, 6, 8, 9],
    [0, 1, 2, 3, 4, 5, 7, 8, 9],
    [0, 1, 2, 3, 4, 6, 7, 8, 9],
    [0, 1, 2, 3, 5, 6, 7, 8, 9],
    [0, 1, 2, 4, 5, 6, 7, 8, 9],
    [0, 1, 3, 4, 5, 6, 7, 8, 9],
    [0, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]
