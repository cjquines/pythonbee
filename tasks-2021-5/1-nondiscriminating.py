"""
Write a function f that takes in a string and returns True if it is non-discriminating and False if it is not.

A string is non-discriminating if each of its characters appears the same number of times and at least twice.

The string will be non-empty and consist of at most 100 lowercase English letters.
"""

# from https://codegolf.stackexchange.com/questions/156967/non-discriminating-programming

def f(s):
    return all(s.count(c) >= 2 for c in s) and len(set(s.count(c) for c in s)) == 1

tests = [
    "racecare",
    "mit",
    "abcdedcba",
    "abacacba",
    "afflffa",
    "afflff",
    "abbaabb",
    "abcdef",
    "afflgflgafa",
    "funggunf",
    "amanaplanaccanalpanama",
    "a"*100,
    "a"*51 + "b"*49
]
