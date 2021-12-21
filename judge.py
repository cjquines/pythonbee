import copy
import enum
import multiprocessing
import importlib
import inspect
import shutil
import sys

try:
    import termcolor

    cprint = termcolor.cprint
except:
    cprint = lambda x, y: print(x)

VERBOSE = False
TIMEOUT = 1
Verdict = enum.Enum("Verdict", "OK WA TL RE PE CE")


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


def judge_case(inp, proc, checker, jout):
    try:
        tout = proc.get(TIMEOUT)
    except multiprocessing.TimeoutError:
        return Verdict.TL, None
    except:
        return Verdict.RE, None
    try:
        if n_args(checker)[1] <= 2:
            verdict = checker(inp, tout)
        else:
            verdict = checker(inp, tout, jout)
        return Verdict.OK if verdict else Verdict.WA, tout
    except:
        return Verdict.PE, tout


def print_data(data):
    # 7 becuase "judge: " is 6 chars, then -1
    cols = shutil.get_terminal_size().columns - 7
    out = str(data)
    # 3 because "..." is 3 chars
    if not VERBOSE and len(out) > cols - 3:
        out = out[: (cols - 3)] + "..."
    return out


def judge(test_f, judge_f, tests, checker, to_splat=False):
    if judge_f:
        to_splat = n_args(judge_f)[1] > 1
    tot_passed = 0
    with multiprocessing.Pool() as pool:
        for inp in tests:
            jinp, tinp = copy.deepcopy(inp), copy.deepcopy(inp)
            proc = pool.apply_async(test_f, tinp if to_splat else (tinp,))
            if judge_f:
                jout = judge_f(*jinp) if to_splat else judge_f(jinp)
            else:
                jout = None
            verdict, tout = judge_case(inp, proc, checker, jout)
            if test_f is None:
                verdict = Verdict.CE
            passed = verdict == Verdict.OK
            tot_passed += passed
            cprint(
                f"   {str(verdict)[-2:]}: {print_data(inp)}",
                "green" if passed else "red",
            )
            if tout is not None:
                print(f" test: {print_data(tout)}")
            if jout is not None:
                print(f"judge: {print_data(jout)}")
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
    return judge(test_f, judge_f, tests, lambda _, tout, jout: tout == jout)


if __name__ == "__main__":
    file = sys.argv[1]
    try:
        test_f = importlib.import_module("responses." + file).f
    except:
        test_f = None
    judge_file = importlib.import_module("judge." + file)
    main(test_f, judge_file)
