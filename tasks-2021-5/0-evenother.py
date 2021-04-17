"""
Write a function f that takes in a list of integers and returns the same list, with each element replaced with True if the other elements sum to an even number, and False otherwise.

For example, the output for [1, 2, 3, 1] should be [True, False, True, True].

The input consists of at least 2 and at most 100 positive integers.
"""

# https://codegolf.stackexchange.com/questions/118505/parity-of-sum-of-other-elements

def f(A):
    return [(sum(A) - x) % 2 == 0 for x in A]

tests = [
    [1, 2, 3, 1],
    [1, 2, 3, 2, 1],
    [2, 2],
    [100, 201, 300, 400],
    [89]*100
]
