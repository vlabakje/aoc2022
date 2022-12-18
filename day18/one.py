def gen_coords(filename):
    with open(filename) as fileh:
        for line in fileh:
            yield tuple(map(int, line.strip().split(",")))


def surface_area(filename):
    coords = set(gen_coords(filename))
    def neigh(c):
        # all six neighs of c
        for x in (-1, 1):
            yield (c[0]+x, c[1], c[2])
        for y in (-1, 1):
            yield (c[0], c[1]+y, c[2])
        for z in (-1, 1):
            yield (c[0], c[1], c[2]+z)
    for c in coords:
        for n in neigh(c):
            #print(f"{c=} {n=} {n in coords=}")
            if n not in coords:
                yield 1


if __name__ == "__main__":
    print(sum(surface_area("small")))
    print(sum(surface_area("example")))
    print(sum(surface_area("input")))
