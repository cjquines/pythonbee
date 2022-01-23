import itertools
import os
import shutil


def copy(inpf, outf):
    """
    Copy file inpf to path outf.
    """
    shutil.copy(inpf, os.path.join("judge", outf))
    with open(inpf, "r", encoding="UTF-8") as fin:
        with open(os.path.join("responses", outf), "w", encoding="UTF-8") as fout:
            count = 0
            marker = '"""\n'
            for line in fin.readlines():
                fout.write(line)
                if line == marker:
                    count += 1
                if count == 2:
                    fout.write("\n")
                    return


def clean():
    """
    Remove files from judge and responses folder.
    """
    for folder in ["judge", "responses"]:
        for file in os.scandir(folder):
            if file.name.rstrip(".py").isdigit():
                os.remove(file)


def main(tasks):
    """
    Copy each task in tasks.
    """
    tasks = filter(lambda t: t[0].isdigit(), tasks)
    for stage, files in itertools.groupby(tasks, key=lambda t: t[0]):
        for task, file in enumerate(files):
            for contestant in "01":
                inpf = os.path.join("tasks", file)
                outf = f"{stage}{task}{contestant}.py"
                copy(inpf, outf)


if __name__ == "__main__":
    clean()
    main(sorted(os.listdir("tasks")))
