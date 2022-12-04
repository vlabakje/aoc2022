def pairs(filename):
    with open(filename) as fileh:
        for line in fileh:
            if line.strip():
                one, two = line.strip().split(',', 1)
                yield tuple(map(int, one.split('-'))), tuple(map(int, two.split('-')))

def overlap(one, two):
    if one[0] > two[0]:  # always make 1 start first
        one, two = two, one
    return one[1] >= two[0]

def overlap_count(filename):
    for one, two in pairs(filename):
        if overlap(one, two):
            yield 1

if __name__ == "__main__":
    print(sum(overlap_count("example")))
    print(sum(overlap_count("input")))
