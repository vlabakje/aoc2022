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
            parts = line.strip().split()
            if parts[0] == "$" and parts[1] == "cd":
                if parts[2] == "..":
                    current = current.parent
                else:
                    current = current.subdirs[parts[2]]
            elif parts[1] == "ls":
                pass
            elif parts[0] == "dir":
                current.subdirs[parts[1]] = Directory(parts[1], current)
            else:
                current.files[parts[1]] = int(parts[0])
    return root


def main(filename):
    root = parse_listing(filename)
    unused = 70000000 - root.size()
    for value in sorted(s for s in root.size_generator()):
        if value + unused >= 30000000:
            return value
    

print(main("example"))
print(main("input"))
