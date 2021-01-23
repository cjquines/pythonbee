"""
Write a function f that takes in a string s and returns a string with the same length as s, but not equal to s.

Both the input and output strings must be non-empty and consist of at most 100 lowercase English letters.
"""

def f(s):
    return ('a' if s[0] != 'a' else 'b') + s[1:]

tests_ = [
    "asdfghwer",
    "jksdfhgiqweadfasdf",
    "b",
    "jqweposiucvomwerawsrf",
    "a"*100,
    "b"*99 + "a",
    "a" + "b"*99,
    "rereqqqpjadsf"
]

def tests(test_f):
    score = 0
    for s in tests_:
        res = test_f(s)
        verdict = res.isalpha() and res.islower() and res != s and len(res) == len(s)
        score += verdict
        print(f"{'OK' if verdict else 'WRONG'}: {s}")
        print(f"   test: {res}")
    print(f"passed {score} out of {len(tests_)}")
