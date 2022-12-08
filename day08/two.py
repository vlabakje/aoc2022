class Tree():
    def __init__(self, data, cols, rows):
        self._data = data
        self._cols = cols
        self._rows = rows

    def get(self, x, y):
        return self._data[self._cols * y + x]

    def scenic_score(self, x, y):
        own = self.get(x, y)
        s1 = s2 = s3 = s4 = 0
        for x_ in range(0, x)[::-1]:  # left
            s1 += 1
            if self.get(x_, y) >= own:
                break
        for x_ in range(x+1, self._cols):  # right
            s2 += 1
            if self.get(x_, y) >= own:
                break
        for y_ in range(0, y)[::-1]:  # up
            s3 += 1
            if self.get(x, y_) >= own:
                break
        for y_ in range(y+1, self._rows):  # down
            s4 += 1
            if self.get(x, y_) >= own:
                break
        return s1 * s2 * s3 * s4

    def max_scenic_score(self):
        return max(self.scenic_score(x, y) for x in range(self._cols) for y in range(self._rows))


def read_tree(filename):
    with open(filename) as fileh:
        lines = fileh.read().strip().split("\n")
        return Tree("".join(l for l in lines), len(lines[0]), len(lines))


print(read_tree("example").max_scenic_score())
print(read_tree("input").max_scenic_score())
