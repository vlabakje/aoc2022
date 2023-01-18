def pairs(filename):
    with open(filename) as fileh:
        for line in fileh:
            one, two = line.strip().split(',', 1)
            yield tuple(map(int, one.split('-'))), tuple(map(int, two.split('-')))

def fully_contains(one, two):
    return one[0] >= two[0] and one[1] <= two[1]

def full_contains_count(filename):
    for one, two in pairs(filename):
        if fully_contains(one, two) or fully_contains(two, one):
            yield 1

if __name__ == "__main__":
    print(sum(full_contains_count("example")))
    print(sum(full_contains_count("input")))
