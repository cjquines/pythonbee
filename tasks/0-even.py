"""
Write a function f that takes in a list of integers and returns the number of even integers in the list.
"""

def f(a):
	return len([x for x in a if x % 2 == 0])

tests = [
    [],
    [2002],
    [2021],
    [1, 9, 23, 5],
    [26, 1, 0, 3, 4],
    [100000000, 2000000001, 3000000000, 40000000],
    [89]*100,
]
