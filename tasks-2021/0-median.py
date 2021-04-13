"""
Write a function f that takes in a list of integers and returns its median.

The list will be non-empty, sorted, and have odd length.
"""

def f(a):
	return a[len(a) // 2]

tests = [
    [1],
    [2056],
    [89, 1234, 591234],
    [58, 12345, 68394],
    [8, 9, 12345, 86139044521, 432481238418234],
    list(range(999))
]
