import queue

def gen_coords(filename):
    with open(filename) as fileh:
        for line in fileh:
            yield tuple(map(int, line.strip().split(",")))


def neigh(c):
    # all six neighs of c
    for x in (-1, 1):
        yield (c[0]+x, c[1], c[2])
    for y in (-1, 1):
        yield (c[0], c[1]+y, c[2])
    for z in (-1, 1):
        yield (c[0], c[1], c[2]+z)


def first(coords):
    x, y, _ = list(coords)[0]
    for z in range(0, 500000):
        if (x, y, z) in coords:
            break
    return (x, y, z-1)


def ext_surface_area(filename):
    min_x = min_y = min_z = 2**32
    max_x = max_y = max_z = 0
    coords = set(gen_coords(filename))
    for c in coords:
        min_x, max_x = min(c[0], min_x), max(c[0], max_x)
        min_y, max_y = min(c[1], min_y), max(c[1], max_y)
        min_z, max_z = min(c[2], min_z), max(c[2], max_z)
    remaining = queue.Queue()
    visited = set()
    # start at the middle of a face, move down until you hit a surface
    start = first(coords)
    remaining.put(start)
    visited.add(start)
    # first node found, it neighbors the blob, now circumnavigate it
    while not remaining.empty():
        c = remaining.get()
        for n in neigh(c):
            if n in visited:
                continue
            if n in coords:
                yield 1
            elif ((min_x-1) <= n[0] <= (max_x+1)) and ((min_y-1) <= n[1] <= (max_y+1)) and ((min_z-1) <= n[2] <= (max_z+1)):
                remaining.put(n)
                visited.add(n)

if __name__ == "__main__":
    #print(sum(ext_surface_area("small")))
    print(sum(ext_surface_area("example")))
    print(sum(ext_surface_area("input")))
