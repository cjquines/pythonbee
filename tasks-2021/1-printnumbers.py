"""
Write a function f that takes no input and returns the list of integers
[
	1,
	22,
	333,
	4444,
	55555,
	666666,
	7777777,
	88888888,
	999999999
].
Note that this is a list of integers, not strings.
"""

def f():
	return list(map(int, "1 22 333 4444 55555 666666 7777777 88888888 999999999".split()))

def checker(test_f):
	verdict = test_f() == f()
	print("OK" if verdict else "WRONG")
	print(f" test: {test_f()}")
	print(f"judge: {f()}")
