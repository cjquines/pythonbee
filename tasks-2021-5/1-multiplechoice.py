"""
Write a function f that takes in two binary arrays A and B, of the same length, and returns a string of the same length, such that its ith character is:
- "a", if the ith entry of A is 1,
- "b", if the ith entry of B is 1,
- "c", otherwise.

Arrays A and B are non-empty and consist of at most 100 entries, each of which are 0 or 1. There is no i such that the ith entry of A and B are both 1.
"""

# https://codegolf.stackexchange.com/questions/69770/cheating-a-multiple-choice-test

def f(A, B):
    return "".join("cab"[a - b] for a, b in zip(A, B))

tests = [
    ([1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0]),
    ([0, 0, 0, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0]),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
]
