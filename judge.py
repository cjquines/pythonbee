import importlib, inspect, sys

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

def judge(test_f, judge_f, tests, checker, to_splat=False):
    if judge_f:
        if not compatible(test_f, judge_f):
            print("signatures for test and judge don't match")
            print(f"(test wants {n_args(test_f)} args)")
            print(f"(judge wants {n_args(judge_f)} args)")
            return
        to_splat = n_args(judge_f)[1] > 1
    tot_passed = 0
    for inp in tests:
        tout = test_f(*inp) if to_splat else test_f(inp)
        if judge_f:
            jout = judge_f(*inp) if to_splat else judge_f(inp)
        if n_args(checker)[1] <= 2:
            verdict = checker(inp, tout)
        else:
            verdict = checker(inp, tout, jout)
        tot_passed += verdict
        print(f"   {'OK' if verdict else 'WA'}: {inp}")
        print(f" test: {tout}")
        if judge_f:
            print(f"judge: {jout}")
        print("")
    print(f"passed {tot_passed} out of {len(tests)}")

def main(test_f, jf):
    get_jf = lambda attr: getattr(jf, attr) if hasattr(jf, attr) else None
    checker = get_jf("checker")
    judge_f = get_jf("f")
    tests = get_jf("tests")

    if checker and not callable(checker):
        raise Exception("expected checker to be callable")
    if checker and n_args(checker)[0] == 1:
        return checker(test_f)
    if not tests:
        raise Exception("expected to have tests")
    if checker:
        return judge(test_f, judge_f, tests, checker)
    if not judge_f:
        raise Exception("expected to have judge f")
    return judge(test_f, judge_f, tests, lambda inp, tout, jout: tout == jout)

if __name__ == "__main__":
    file = sys.argv[1]
    test_f = importlib.import_module("responses." + file).f
    judge_file = importlib.import_module("judge." + file)
    main(test_f, judge_file)
