"""
Write a function f that takes in a positive integer n. The output should be the number of positive integers between 1 and n, inclusive, whose base-10 representation ends with the digit 2.
"""

def f(n):
	return len([x for x in range(n + 1) if x % 10 == 2])

tests = [1, 2, 5, 20, 100, 999, 992, 991]
