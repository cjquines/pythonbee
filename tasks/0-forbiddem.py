"""
Write a function f that takes in a string and returns the same string, with all "n"s replaced with "m"s.

The string will be non-empty and consist of at most 100 lowercase English characters.
"""

def f(s):
	return s.replace("n", "m")

tests = [
    "delicious",
    "mit",
    "content",
    "n",
    "n"*100,
    "m"*55 + "n"*45,
    "antecedent",
    "amsterdam",
]
