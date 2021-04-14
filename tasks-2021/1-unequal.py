"""
Write a function f that takes in a string s and returns a string with the same length as s, but not equal to s.

Both the input and output strings must be non-empty and consist of at most 100 lowercase English letters.
"""

def f(s):
    return ('a' if s[0] != 'a' else 'b') + s[1:]

tests = [
    "asdfghwer",
    "jksdfhgiqweadfasdf",
    "b",
    "jqweposiucvomwerawsrf",
    "a"*100,
    "b"*99 + "a",
    "a" + "b"*99,
    "rereqqqpjadsf"
]

def checker(inp, tout):
    conds = [
        tout.isalpha(),
        tout.islower(),
        tout != inp,
        len(tout) == len(inp)
    ]
    return all(conds)
