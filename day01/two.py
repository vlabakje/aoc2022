def elves(filename):
    with open(filename) as fileh:
        for elf in fileh.read().strip().split("\n\n"):
            yield sum(map(int, elf.split("\n")))

print(sum(sorted(elves("example"))[-3:]))
print(sum(sorted(elves("input"))[-3:]))
