class Tree():
    def __init__(self, data, cols, rows):
        self._data = data
        self._cols = cols
        self._rows = rows

    def get(self, x, y):
        return self._data[self._cols * y + x]

    def is_visible(self, x, y):
        if x in (0, self._rows-1) or y in (0, self._cols-1):  # edges
            return True
        own = self.get(x, y)
        return any((
                all(own > self.get(x_, y) for x_ in range(0, x)),  # left
                all(own > self.get(x_, y) for x_ in range(x+1, self._cols)),  # right
                all(own > self.get(x, y_) for y_ in range(0, y)),  # up
                all(own > self.get(x, y_) for y_ in range(y+1, self._rows))  # down
                ))

    def visible_count(self):
        visible = self._cols * self._rows
        for x in range(self._cols):
            for y in range(self._rows):
                if not self.is_visible(x, y):
                    visible -= 1
        return visible

def read_tree(filename):
    with open(filename) as fileh:
        lines = fileh.read().strip().split("\n")
        return Tree("".join(l.strip() for l in lines), len(lines[0].strip()), len(lines))


def main(filename):
    tree = read_tree(filename)
    return tree.visible_count()


print(main("example"))
print(main("input"))
