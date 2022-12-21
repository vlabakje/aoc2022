def solve(filename):
    l = dict()
    with open(filename) as fileh:
        lines = [line.strip().replace(":", " =") for line in fileh.readlines()]
        while len(lines):
            line = lines.pop(0)
            try:
                out = exec(line, l)
            except NameError:
                lines.append(line)
    return l["root"]

print(solve("example"))
print(solve("input"))
