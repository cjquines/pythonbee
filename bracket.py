import random


def main():
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
    main()
