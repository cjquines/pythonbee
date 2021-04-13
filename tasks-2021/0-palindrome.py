"""
Write a function f that takes in a string and returns True if it is a palindrome and False if it is not.

A palindrome is spelled the same forwards and backwards. "racecar" is a palindrome, "mit" is not.

The string will be non-empty and consist of at most 100 lowercase English letters.
"""

def f(s):
	return s == s[::-1]

tests = [
    "racecar",
    "mit",
    "abcdedcba",
    "abacaba",
    "afflffa",
    "afflff",
    "abddba",
    "afflgfa",
    "funggunf",
    "amanaplanacanalpanama",
    "a"*100,
    "a"*99 + "b"
]
