"""
Write a function f that takes in an array of integers and returns an array with the same elements, but is neither sorted nor sorted in reverse.

The array will have at least 3 and at most 100 distinct positive integers.
"""

def f(a):
    a.sort()
    return [a[1]] + [a[0]] + a[2:]

tests = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 3, 2],
    [8, 1234, 59234, 432, 591],
    list(range(1, 101))
]

def checker(s, res):
    return set(res) == set(s) and res != sorted(s) and res != sorted(s, reverse=True)
