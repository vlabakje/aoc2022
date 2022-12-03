def rucksacks(filename):
    with open(filename) as fileh:
        for line in fileh:
            if line.strip():
                yield line.strip()


def rearrange(filename):
    for rucksack in rucksacks(filename):
        common = set(rucksack[:len(rucksack)//2]) & set(rucksack[len(rucksack)//2:])
        assert len(common) == 1, f"unexpected {common=} {rucksack=}"
        priority = ord(list(common)[0])
        yield priority - (96 if priority > 96 else 38)


print(sum(rearrange("example")))
print(sum(rearrange("input")))
