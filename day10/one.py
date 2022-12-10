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


def signals(filename):
    X = 1
    for cycle, effect in cycle_effect(filename):
        if ((cycle - 20) % 40) == 0:
            print(f"{cycle=} {X=} {X*cycle=}")
            yield X*cycle
        X += effect


print(sum(signals("example")))
print(sum(signals("input")))
