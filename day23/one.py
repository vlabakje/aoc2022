import collections

DIRECTION_OFFSET = {
        "north": ((-1, -1), (0, -1), (1, -1)),
        "south": ((-1, 1,), (0, 1), (1, 1)),
        "west": ((-1, -1), (-1, 0), (-1, 1)),
        "east": ((1, -1), (1, 0), (1, 1))}


def add(x, y, offset):
    return (x+offset[0], y+offset[1])

class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.intent = None

    def propose(self, order, occupation):
        direction = (-1, 0)
        n = 0
        for o_y in (-1, 0, 1):
            for o_x in (-1, 0, 1):
                if add(self.x, self.y, (o_x, o_y)) in occupation:
                    n += 1
        if n == 1:
            return
        for o in order:
            if all(add(self.x, self.y, offset) not in occupation for offset in DIRECTION_OFFSET[o]):
                self.intent = add(self.x, self.y, DIRECTION_OFFSET[o][1])
                yield self.intent
                return

def read_elves(filename):
    with open(filename) as fileh:
        for y, line in enumerate(fileh):
            for x, c in enumerate(line):
                if c == "#":
                    yield Elf(x, y)

def round(elves, order):
    occupation = set((elf.x, elf.y) for elf in elves)
    proposed = collections.Counter()
    for elf in elves:
        proposed.update(elf.propose(order, occupation))
    #print(proposed)
    # second part
    for elf in elves:
        if elf.intent != None and proposed[elf.intent] == 1:
            elf.x, elf.y = elf.intent
        elf.intent = None

def print_elves(elves):
    occupation = set((elf.x, elf.y) for elf in elves)
    min_x = max_x = min_y = max_y = 0
    for elf in elves:
        min_x, max_x = min(min_x, elf.x), max(max_x, elf.x)
        min_y, max_y = min(min_y, elf.y), max(max_y, elf.y)
    #print(f"{min_x=},{min_y=}")
    for y in range(min_y, max_y+1):
        line = ""
        for x in range(min_x, max_x+1):
            line += "#" if (x, y) in occupation else "."
        print(line)
    return ((max_y-min_y+1) * (max_x-min_x+1)) - len(elves)

def smallest_rect(filename):
    elves = list(read_elves(filename))
    #print_elves(elves)
    order = ["north", "south", "west", "east"]
    for i in range(10):
        #print(f"{order[0]=}")
        round(elves, order)
        order.append(order.pop(0))
        print(f"== End of round {i+1}")
        #x = print_elves(elves)
    return print_elves(elves)


print(smallest_rect("input"))
