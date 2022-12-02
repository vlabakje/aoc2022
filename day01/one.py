def elves(filename):
    with open(filename) as fileh:
        for elf in fileh.read().strip().split("\n\n"):
            yield sum(map(int, elf.split("\n")))

print(max(elves("example")))
print(max(elves("input")))
