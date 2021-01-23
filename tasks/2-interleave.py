"""
Write a function f that takes in a positive integer n. The output should be the integer result of interleaving the integers from 1 to n with the integers from n to 1.

For example, if the input is 4, the output should be 14233241.

Outputting either a string or an integer is acceptable.
"""

def f(n):
    return "".join(f"{a}{b}" for a, b in zip(range(1, n+1), range(n, 0, -1)))

tests_ = [1, 4, 10, 32, 100]

def tests(test_f):
    tot_passed = 0
    for inp in tests_:
        tout, jout = str(test_f(inp)), f(inp)
        verdict = tout == jout
        tot_passed += verdict

        print(f"{'OK' if verdict else 'WRONG'}: {inp}")
        print(f"   test: {tout}")
        print(f"  judge: {jout}")
        print("")
    print(f"passed {tot_passed} out of {len(tests)}")
