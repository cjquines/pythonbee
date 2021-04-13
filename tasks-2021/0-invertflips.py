"""
Write a function f that takes in a string of coin flips and returns the string with the flips inverted.

For example, with the input "HHTH", the output should be "TTHT".

The string will be non-empty and consist of at most 100 characters, each of which are "H" or "T".
"""

def f(s):
    return "".join({"H": "T", "T": "H"}[c] for c in s)

tests = [
    "HHTH",
    "H",
    "T",
    "HH"*30 + "TT",
    "H"*50 + "T"*50,
    "H"*100
]
