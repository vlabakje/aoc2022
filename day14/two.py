import enum
import itertools

SAND_ORIGIN = (500, 0)

class Field(enum.Enum):
    EMPTY = 0
    ROCK = 1
    SAND = 2
    FLOOR = 3

class FellOffException(Exception):
    pass

class Grid():
    def __init__(self, filename):
        self.x = SAND_ORIGIN[0]*2
        self.y = 0
        instructions = []
        lines = []
        with open(filename) as fileh:
            for line in fileh:
                self.y = max(self.y, max(int(pair.split(',')[1]) for pair in line.strip().split(" -> ")))
                lines.append(line.strip())
        self.y +=2
        self._g = [Field.EMPTY] * self.x * (self.y)
        self._g += [Field.FLOOR] * self.x
        for line in lines:
            for a, b in itertools.pairwise(line.split(" -> ")):
                a, b = tuple(map(int, a.split(","))), tuple(map(int, b.split(",")))
                if a[0] == b[0]:
                    for y in range(min(a[1], b[1]), max(a[1], b[1])+1):
                        self.set(a[0], y, Field.ROCK)
                elif a[1] == b[1]:
                    for x in range(min(a[0], b[0]), max(a[0], b[0])+1):
                        self.set(x, a[1], Field.ROCK)
                else:
                    raise NotImplementedError("not a straight line")

    def get(self, x, y):
        return self._g[self.x*y+x]

    def set(self, x, y, value):
        self._g[self.x*y+x] = value

    def print(self, min_x, max_x):
        for y in range(self.y+1):
            line = ""
            for x in range(min_x, max_x+1):
                match self.get(x, y):
                    case Field.EMPTY:
                        line += "."
                    case Field.ROCK:
                        line += "#"
                    case Field.SAND:
                        line += "o"
                    case Field.FLOOR:
                        line += "="
            print(line)

    def grains(self):
        try:
            for i in range(1, 2**16):
                x, y = self.grain_drop()
                if (x, y) == SAND_ORIGIN:
                    return i
                self.set(x, y, Field.SAND)
        except FellOffException:
            return i

    def grain_drop(self):
        x = SAND_ORIGIN[0]
        for y in range(self.y):
            if self.get(x, y+1) == Field.EMPTY:
                pass
            elif self.get(x-1, y+1) == Field.EMPTY:
                x -= 1
            elif self.get(x+1, y+1) == Field.EMPTY:
                x += 1
            else:
                return x, y
        raise FellOffException(f"{x=} {y=}")

if __name__ == "__main__":
    g = Grid("example")
    #g.print(494, 503)
    print("example ", g.grains())
    #g.print(480, 520)
    g = Grid("input")
    print("input ", g.grains())
    #g.print(0, 999)
