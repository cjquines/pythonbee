from importlib import import_module
import sys

file = sys.argv[1]

test_f = import_module("responses." + file).f
judge_f = import_module("judge." + file).f
tests = import_module("judge." + file).tests

if callable(tests):
    tests(test_f)
else:
    tot_passed = 0
    for inp in tests:
        tout, jout = test_f(inp), judge_f(inp)
        verdict = tout == jout
        tot_passed += verdict

        print(f"{'OK' if verdict else 'WRONG'}: {inp}")
        print(f"   test: {tout}")
        print(f"  judge: {jout}")
        print("")
    print(f"passed {tot_passed} out of {len(tests)}")
