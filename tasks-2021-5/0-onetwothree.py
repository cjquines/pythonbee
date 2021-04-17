"""
Write a function f that takes in a positive integer n and returns True if it's in the following list, and False if it isn't:
[123, 234, 345, 456, 567, 678, 789].

The input will be at most 10000.
"""

# https://codegolf.stackexchange.com/questions/91599/as-easy-as-one-two-three

def f(n):
    return n in list(range(123, 790, 111))

tests = [
    123,
    234,
    678,
    789,
    12,
    1,
    2,
    1234
]
