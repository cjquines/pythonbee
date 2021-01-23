# pythonbee

very quickly hacked-together code for running the nth annual python bee.

this is set up for a single-elimination matchup tournament, where each round consists of a one on one matchup with two contestants doing the same programming task.

how to run a python bee:

- send out [the rules](https://docs.google.com/document/d/1VZOJnWJz8sSLwztIcknc5Mn16ktyCO06L_nFS60YcEU/edit), possibly revising them if you have other thoughts.

- write [the tasks](https://github.com/cjquines/pythonbee/tree/master/tasks). the filename should be `roundnumber-puzzletitle.py`. the format should be a triple-quoted string with the problem description, followed by the judge's solution, followed by the tests.

- the given judge assumes that the task is to always write a function named `f`. the tests should be a list of inputs to the function that will be compared against both the judge's solution and the contestant's solution, although sometimes you might need to add [a custom checker](https://github.com/cjquines/pythonbee/blob/master/tasks/1-unequal.py).

- once you're done writing the tasks, run `gen.py` to generate the files. this will generate files in the `judge` folder and the `responses` folder.

- contestants write their code in the corresponding files in the `responses` folder. the filenames are of the form `123.py`, where `1` is the round number, `2` is the problem number, and `3` is the contestant number; these are intentionally nondescript file names.

- run `judge.py 123` to run the tests for `responses/123.py`.

this is sketchy infra i am accepting PRs
