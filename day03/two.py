def groups(filename):
    with open(filename) as fileh:
        lines = list(line.strip() for line in fileh.readlines())
        for i in range(len(lines)//3):
            yield lines[i*3:i*3+3]


def sticker_prios(filename):
    for group in groups(filename):
        one, two, three = map(set, group)
        priority = ord(list(one & two & three)[0])
        yield priority - (96 if priority > 96 else 38)


print(sum(sticker_prios("example")))
print(sum(sticker_prios("input")))
