def pairs(filename):
    with open(filename) as fileh:
        for line in fileh:
            if line.strip():
                one, two = line.strip().split(',', 1)
                yield tuple(map(int, one.split('-'))), tuple(map(int, two.split('-')))

def fully_contains(one, two):
    if one[0] > two[0]:  # always make 1 start first
        one, two = two, one
    if one[1] < two[0]:  # there is no overlap at all
        return False
    if one[1] >= two[1] or one[0] == two[0]:  # there is overlap
        return True

def full_contains_count(filename):
    for one, two in pairs(filename):
        if fully_contains(one, two):
            yield 1

if __name__ == "__main__":
    print(sum(full_contains_count("example")))
    print(sum(full_contains_count("input")))
