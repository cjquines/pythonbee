"""
Write a function f that takes in two positive integers, representing ages, and returns True if it represents a creepy relationship and False if it does not.

A relationship is creepy if the age of one person is strictly less than half the age of the other person plus seven. For example, (50, 15) is creepy, because 15 < 50/2 + 7.
"""

# https://codegolf.stackexchange.com/questions/122520/is-this-relationship-creepy

def f(a, b):
    return min(a, b) < max(a, b) / 2 + 7

tests = [
    (40, 40),
    (18, 21),
    (80, 32),
    (15, 50),
    (47, 10000),
    (37, 38),
    (22, 18),
    (50, 15),
    (13, 13),
]
