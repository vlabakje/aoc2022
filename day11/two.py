import functools

class Monkey:
    def __init__(self, text):
        lines = [l.strip() for l in text.split("\n")]
        assert lines[0].startswith("Monkey ")
        self.items = list(map(int, lines[1].split(": ")[1].split(",")))
        op_parts = lines[2].split(" ")
        assert op_parts[0] == "Operation:"
        if op_parts [-1] == "old":
            self.operation = lambda x: x*x
        elif op_parts[-2] == "+":
            self.operation = lambda old: old + int(op_parts[-1])
        elif op_parts[-2] == "*":
            self.operation = lambda x: x * int(op_parts[-1])
        else:
            raise Exception(line[2])
        assert lines[3].startswith("Test: divisible by"), lines[3]
        # self.test = lambda x: x % int(lines[3].split(" ")[-1]) == 0
        self.test_n = int(lines[3].split(" ")[-1])
        self.true = int(lines[4].split(" ")[-1])
        self.false = int(lines[5].split(" ")[-1])
        self.inspected = 0

    def play_round(self, divider):
        while len(self.items):
            # print("\tstarting with ", self.items[0])
            self.inspected += 1
            worry = self.operation(self.items.pop(0)) % divider
            if worry % self.test_n == 0:
                yield self.true, worry
            else:
                yield self.false, worry



def read_monkeys(filename):
    output = {}
    with open(filename) as fileh:
        for i, text in enumerate(fileh.read().split("\n\n")):
            output[i] = Monkey(text)
    return output


def main(filename):
    monkeys = read_monkeys(filename)
    divider = functools.reduce(lambda x, y: x*y, (m.test_n for m in monkeys.values()))
    for r in range(10000):
        print(f"=== round {r} ===")
        for i in range(len(monkeys)):
            # print(f"monkey {i}")
            for to, value in monkeys[i].play_round(divider):
                monkeys[to].items.append(value)
                # print(f"\t{to=} {value=}")
    for i, m in monkeys.items():
        print(f"Monkey {i} {m.inspected=}")
    a, b = sorted(m.inspected for m in monkeys.values())[-2:]
    return a * b

# print(main("example"))
print(main("input"))
