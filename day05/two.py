def stacks_moves(filename):
    with open(filename) as fileh:
        stack_lines, moves = fileh.read().split("\n\n")
        stack_lines = stack_lines.rstrip().split("\n")
        # last number on last line is stack count
        stack_count = int(stack_lines[-1].split(" ")[-1])
        stacks = [list() for _ in range(stack_count)]
        # 1 > 1, 2 > 5, 3 > 9  # (n - 1) * 4  + 1
        for c in stack_lines[:-1][::-1]:
            for i in range(stack_count):
                col = i * 4 + 1
                if len(c) > col and c[col] != " ":
                    stacks[i].append(c[col])
        return stacks, moves

def rearrange(filename):
    stacks, moves = stacks_moves(filename)
    for move in moves.strip().split("\n"):
        _, n, _, source, _, target = move.split(" ")
        t = []
        for i in range(int(n)):
            t.append(stacks[int(source)-1].pop())
        for i in t[::-1]:
            stacks[int(target)-1].append(i)
    return "".join(s[-1] for s in stacks)

print(rearrange("example"))
print(rearrange("input"))
