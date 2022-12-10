import sys

def cycle_effect(filename):
    cycle = 1
    with open(filename) as fileh:
        for line in fileh:
            match line.strip().split(" "):
                case ["addx", arg]:
                    yield cycle, 0
                    cycle += 1
                    yield cycle, int(arg)
                case ["noop"]:
                    yield cycle, 0
                case _:
                    print(f"unable to match {line=}")
            cycle += 1


def draw(filename):
    X = 1
    for cycle, effect in cycle_effect(filename):
        px = (cycle-1) % 40
        sys.stdout.write("#" if px in (X-1, X, X+1) else ".")
        X += effect
        if cycle % 40 == 0:
            sys.stdout.write("\n")

draw("example")
draw("input")
