"""
Write a function f that takes in an integer n between 1 and 26, inclusive. The output should be the first n letters of the string "abcdefghijklmnopqrstuvwxyz".
"""

def f(n):
    return "abcdefghijklmnopqrstuvwxyz"[:n]

tests = list(range(1, 26))
