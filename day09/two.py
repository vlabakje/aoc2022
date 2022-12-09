def instructions(filename):
    with open(filename) as fileh:
        for line in fileh:
            if line.split():
                direction, length = line.split(" ")
                yield direction, int(length)


def print_grid(head, tails):
    min_x = max_x = min_y = max_y = 0
    points = {"H": head, "s": (0, 0)}
    for i, tail in enumerate(tails):
        points[str(i+1)] = tail
    for x, y in points.values():
        min_x, max_x = min(x, min_x), max(x, max_x)
        min_y, max_y = min(y, min_y), max(y, max_y)
    output = [["."]*(1 + max_x - min_x) for _ in range(1+ max_y - min_y)]
    for label, (x, y) in points.items():
        output[y-min_y][x-min_x] = label
    for l in output:
        print("".join(l))

def adjacent(one, two):
    rel_x, rel_y = two[0] - one[0], two[1] - one[1]
    return rel_x in (-1, 0, 1) and rel_y in (-1, 0, 1)


def follow(lead, tail):
    if adjacent(lead, tail):
        return tail
    output = tail[:]
    if lead[0] == tail[0]:  # catch up vertical
        output[1] += 1 if lead[1] > tail[1] else -1
    elif lead[1] == tail[1]:  # catch up horizontal
        output[0] += 1 if lead[0] > tail[0] else -1
    else:  # move diagonal to catch up
        output[1] += 1 if lead[1] > tail[1] else -1
        output[0] += 1 if lead[0] > tail[0] else -1
    return output


def tail_visits(filename):
    head_visited = set()
    tail_visited = set()
    cur_head = [0, 0]
    tails = [[0, 0] for _ in range(9)]
    for direction, length in instructions(filename):
        for _ in range(length):
            match direction:
                case "U":
                    cur_head[1] -= 1
                case "D":
                    cur_head[1] += 1
                case "L":
                    cur_head[0] -= 1
                case "R":
                    cur_head[0] += 1
            head_visited.add(tuple(cur_head))
            for i in range(len(tails)):
                if i == 0:
                    tails[i] = follow(cur_head, tails[i])
                else:
                    tails[i] = follow(tails[i-1], tails[i])
            tail_visited.add(tuple(tails[-1]))
            #print_grid(cur_head, tails)
            #print("---")
    #print_grid(cur_head, tails)
    return len(tail_visited)

print(tail_visits("example"))
print(tail_visits("input"))
