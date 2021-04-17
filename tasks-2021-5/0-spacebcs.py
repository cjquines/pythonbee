"""
Write a function f that takes in an integer n between 1 and 26, inclusive. The output should be the nth string in the following list:
[
    "a",
    " b",
    "  c",
    "   d",
    ...
    "                         z"
].
"""

# from https://codegolf.stackexchange.com/questions/125117/diagonal-alphabet

def f(n):
    n = n - 1
    return " "*n + "abcdefghijklmnopqrstuvwxyz"[n]

tests = list(range(1, 26))
