class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.subdirs = {}
        self._size = None
    
    def size(self):
        if not self._size:
            self._size = sum(self.files.values()) + sum(subdir.size() for subdir in self.subdirs.values())
        return self._size

    def size_generator(self):
        for subdir in self.subdirs.values():
            yield from subdir.size_generator()
        yield self._size

def parse_listing(filename):
    current = root = Directory("", None)
    current.subdirs["/"] = Directory("/", root)
    with open(filename) as fileh:
        for line in fileh:
            match line.split():
                case ['$', 'cd', '..']:
                    current = current.parent
                case ['$', 'cd', name]:
                    current = current.subdirs[name]
                case ['$', 'ls']:
                    pass
                case ['dir', name]:
                    current.subdirs[name] = Directory(name, current)
                case [size, name]:
                    current.files[name] = int(size)
    return root


def main(filename):
    root = parse_listing(filename)
    unused = 70000000 - root.size()
    for value in sorted(s for s in root.size_generator()):
        if value + unused >= 30000000:
            return value
    

print(main("example"))
print(main("input"))
