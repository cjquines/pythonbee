import itertools, os, shutil, subprocess

def copy(inpf, outf):
    shutil.copy(inpf, os.path.join("judge", outf))
    with open(inpf, "r") as fin:
        with open(os.path.join("responses", outf), "w") as fout:
            count = 0
            marker = '"""\n'
            for line in fin.readlines():
                fout.write(line)
                if line == marker:
                    count += 1
                if count == 2:
                    fout.write("\n")
                    return

for r, fs in itertools.groupby(sorted(os.listdir("tasks")), key=lambda t: t[0]):
    for i, f in enumerate(fs):
        for k in "01":
            inpf = os.path.join("tasks", f)
            outf = f"{r}{i}{k}.py"
            copy(inpf, outf)
