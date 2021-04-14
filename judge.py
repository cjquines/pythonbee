from importlib import import_module
import inspect
import sys

def n_args(f):
    parameters = inspect.signature(f).parameters.items()
    nondefault = lambda param: param.default == inspect.Parameter.empty
    min_args = len([name for name, param in parameters if nondefault(param)])
    max_args = len(parameters)
    return min_args, max_args

def compatible(test_f, judge_f):
    min_test, max_test = n_args(test_f)
    min_judge, max_judge = n_args(judge_f)
    return min_test <= min_judge <= max_judge <= max_test

file = sys.argv[1]

test_f = import_module("responses." + file).f
judge_f = import_module("judge." + file).f
tests = import_module("judge." + file).tests

if callable(tests):
    tests(test_f)
elif not compatible(test_f, judge_f):
    print("signatures for test and judge don't match")
    print(f"(test wants {n_args(test_f)} args)")
    print(f"(judge wants {n_args(judge_f)} args)")
else:
    to_splat = n_args(judge_f)[1] > 1
    tot_passed = 0
    for inp in tests:
        if to_splat:
            tout, jout = test_f(*inp), judge_f(*inp)
        else:
            tout, jout = test_f(inp), judge_f(inp)
        verdict = tout == jout
        tot_passed += verdict

        print(f"   {'OK' if verdict else 'WA'}: {inp}")
        print(f" test: {tout}")
        print(f"judge: {jout}")
        print("")
    print(f"passed {tot_passed} out of {len(tests)}")
