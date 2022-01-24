import copy
import enum
import importlib
import inspect
import multiprocessing
import multiprocessing.dummy
import random
import shutil
import sys

try:
    import termcolor

    cprint = termcolor.cprint
except ImportError:
    cprint = lambda x, y: print(x)

VERBOSE = False
TIMEOUT = 1
Verdict = enum.Enum("Verdict", "OK WA TL RE PE CE")


def n_args(func):
    """
    Return (min_args, max_args) of input function.
    """
    parameters = inspect.signature(func).parameters.items()
    nondefault = lambda param: param.default == inspect.Parameter.empty
    min_args = len([name for name, param in parameters if nondefault(param)])
    max_args = len(parameters)
    return min_args, max_args


def compatible(test_f, judge_f):
    """
    Return if judge_f inputs can be called on test_f.
    """
    min_test, max_test = n_args(test_f)
    min_judge, max_judge = n_args(judge_f)
    return min_test <= min_judge <= max_judge <= max_test


def judge_case(inp, proc, checker, jout):
    """
    Judge a thread given by proc, return (Verdict, output).
    """
    try:
        tout = proc.get(TIMEOUT)
    except multiprocessing.TimeoutError:
        return Verdict.TL, None
    except Exception as exc:
        # cprint(exc, "red")
        return Verdict.RE, None
    try:
        if n_args(checker)[1] <= 2:
            verdict = checker(inp, tout)
        else:
            verdict = checker(inp, tout, jout)
        return Verdict.OK if verdict else Verdict.WA, tout
    except Exception as exc:
        # cprint(exc, "red")
        return Verdict.PE, tout


def format_data(data):
    """
    Format the data to fit in terminal, clipping if needed.
    """
    # 7 becuase "judge: " is 6 chars, then -1
    cols = shutil.get_terminal_size().columns - 7
    out = str(data)
    # 3 because "..." is 3 chars
    if not VERBOSE and len(out) > cols - 3:
        out = out[: (cols - 3)] + "..."
    return out


def judge_cases(test_f, judge_f, tests, checker, to_splat=False):
    """
    Compare test_f to judge_f; set to_splat if f should take multiple args.
    Return the score.
    """
    if judge_f:
        to_splat = n_args(judge_f)[1] > 1
    tot_passed = 0
    with multiprocessing.dummy.Pool() as pool:
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
                f"   {str(verdict)[-2:]}: {format_data(inp)}",
                "green" if passed else "red",
            )
            if tout is not None:
                print(f" test: {format_data(tout)}")
            if jout is not None:
                print(f"judge: {format_data(jout)}")
            print("")
    print(f"passed {tot_passed} out of {len(tests)}")
    return tot_passed


def parse_length(test_file):
    """
    Return the length of contestant's program.
    """
    with open(f"responses/{test_file}.py", encoding="UTF-8") as file:
        length = 0
        count = 0
        for line in file.readlines():
            if count >= 2:
                length += len(line)
            if line.strip() == '"""':
                count += 1
    print(f"program length {length}")
    return length


def judge(test_file, test_mod, judge_mod):
    """
    Return score and program length. test_mod and judge_mod should be modules.
    """
    get_func = lambda module, attr: getattr(module, attr, None)
    test_f = get_func(test_mod, "f")
    checker = get_func(judge_mod, "checker")
    judge_f = get_func(judge_mod, "f")
    tests = get_func(judge_mod, "tests")

    if checker and not callable(checker):
        raise Exception("expected checker to be callable")
    if checker and n_args(checker)[0] == 1:
        score = int(checker(test_f))
    elif not tests:
        raise Exception("expected to have tests")
    elif checker:
        score = judge_cases(test_f, judge_f, tests, checker)
    elif not judge_f:
        raise Exception("expected to have judge f")
    else:
        score = judge_cases(test_f, judge_f, tests, lambda _, tout, jout: tout == jout)

    length = parse_length(test_file)
    return score, length


def main(test_file):
    """
    Judge a test_file, assuming it exists.
    """
    try:
        test_mod = importlib.import_module(f"responses.{test_file}")
    except Exception as exc:
        # cprint(exc, "red")
        test_mod = None
    judge_mod = importlib.import_module(f"judge.{test_file}")
    score, length = judge(test_file, test_mod, judge_mod)
    return score, length


def write_bracket():
    """
    Write next bracket for results.md; fails silently.
    """
    with open("results.md", "a+", encoding="UTF-8") as file:
        pass  # create if does not exist
    with open("results.md", "r", encoding="UTF-8") as file:
        kerbs = []
        for line in reversed(file.readlines()):
            if set(line.strip()) == {"-"}:
                break
            kerbs.append(line.strip())
        kerbs = list(filter(None, kerbs))
        random.shuffle(kerbs)
    if not kerbs:
        return
    max_len = max(len(kerb) for kerb in kerbs)
    with open("results.md", "a", encoding="UTF-8") as file:
        while len(kerbs) > 1:
            line = " vs. ".join(
                f"{kerbs.pop().ljust(max_len)}"
                for _ in range(3 if len(kerbs) == 3 else 2)
            ).strip()
            file.write("\n" + line + "\n")
        file.write("\n" + "-" * 34 + "\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        write_bracket()
