# pythonbee

very quickly hacked-together code for running the nth annual python bee. if you're the new person running it, you should ask the previous person who ran it for their unused tasks.

this is set up for a single-elimination matchup tournament, where each round consists of a one on one matchup with two contestants doing the same programming task.

how to run a python bee:

- send out [the rules](https://docs.google.com/document/d/e/2PACX-1vRZlv-Z8PDweCTX8kMz07IKMiu9_QbPaCu1lTipzONOpcFCRD91VXHIZ8OnyAYRyy1y34bZw5GgIRVs/pub), possibly revising them if you have other thoughts.

- write the tasks in the folder [tasks](tasks/). the filename should be `roundnumber-puzzletitle.py`. the format should be a triple-quoted string with the problem description, followed by the judge's solution, followed by the tests. see examples in [tasks-2021](tasks-2021/) and [tasks-2021-5](tasks-2021-5/).

- the given judge assumes that the task is to always write a function named `f`. the tests should be a list of inputs to the function that will be compared against both the judge's solution and the contestant's solution. the checker will inspect the signature of `f`. if it takes in more than one argument, it will splat the input before passing it to `f`. it also supports custom checkers; see [unequal](tasks-2021/1-unequal.py), [printnumbers](tasks-2021/1-printnumbers.py), [interleave](tasks-2021/2-interleave.py).

- once you're done writing the tasks, run `gen.py` to generate the files. this will generate files in the `judge` folder and the `responses` folder.

- contestants write their code in the corresponding files in the `responses` folder. the filenames are of the form `123.py`, where `1` is the round number, `2` is the problem number, and `3` is the contestant number; these are intentionally nondescript file names.

- run `judge.py 123` to run the tests for `responses/123.py`.

this is sketchy infra i am accepting PRs

### thoughts on tasks

each year, for n contestants, you'll need approximately n tasks. (in a 16-person tournament, that's 8 round 0, 4 round 1, 2 round 2, and 1 round 3, which is what i usually prepare for.) thoughts on difficulty:

- you really don't want it to be the case that no one in a matchup has a correct program. the ideal is if only one person in each matchup has a correct program, and the other one does not. failing that, it's better for both contestants to get it correct than neither.

- the rounds should get roughly harder each time, but even the hardest problems should be solvable with one-liners, for some definition of a one-liner. the one-liner solution need not be the most obvious one; harder tasks should have a witty, non-obvious one-liner that involves restating the problem somehow. see [banknote](tasks-2021-5/1-banknote.py).

- actually test your tasks if you can!
