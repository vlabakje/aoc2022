def execute(lines):
    l = dict()
    while len(lines):
        line = lines.pop(0)
        try:
            exec(line, None, l)
        except NameError as ne:
            lines.append(line)
    return l

def root_parts(lines):
    for line in lines:
        if line.startswith("root"):
            parts = line.split("=")[1].strip().split(" ")
            return parts[0], parts[2]

def indexof(lines, prefix):
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            return i

def is_a_changing_humn(lines, humn_i, a, b, a_i, b_i):
    l_before = execute(lines[:])
    a_before = l_before[a]
    b_before = l_before[b]
    lines[humn_i] = "humn = 2"
    l_after = execute(lines)
    a_after = l_after[a]
    b_after = l_after[b]
    assert not (a_before == a_after) and (b_before == b_after), "changing humn didn't change a, b"
    return a_before != a_after

def two(filename, low, high):
    with open(filename) as fileh:
        lines = [line.strip().replace(":", " =") for line in fileh.readlines()]
        a, b = root_parts(lines)
        root_i = indexof(lines, "root")
        a_i = indexof(lines, a)
        b_i = indexof(lines, b)
        humn_i = indexof(lines, "humn")
        if not is_a_changing_humn(lines[:], humn_i, a, b, a_i, b_i):
            a, b = b, a
            a_i, b_i = b_i, a_i
        # change the value of humn to change a to match b
        for _ in range(500):
            avg = (low+high)//2
            lines[humn_i] = f"humn = {avg}"
            l = execute(lines[:])
            print(f"{low=} {high=} {l[a]-l[b]=} {l['humn']=} {l[a]==l[b]=} {l[a]-l[b]=} {l[a]=} {l[b]=}")
            if l[a]-l[b] == 0:
                return avg
            if l[a]-l[b] > 0:
                low = avg
            else:
                high = avg

print(two("example", 301, 301))
print(two("input", 0, 2**64))
