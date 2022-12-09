def instructions(filename):
    with open(filename) as fileh:
        for line in fileh:
            if line.split():
                direction, length = line.split(" ")
                yield direction, int(length)

def adjacent(one, two):
    rel_x, rel_y = two[0] - one[0], two[1] - one[1]
    return rel_x in (-1, 0, 1) and rel_y in (-1, 0, 1)


def tail_visits(filename):
    head_visited = set()
    tail_visited = set()
    cur_head = [0, 0]
    cur_tail = [0, 0]
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
            if not adjacent(cur_head, cur_tail):
                cur_tail = cur_head[:]
                match direction:
                    case "U":
                        cur_tail[1] += 1
                    case "D":
                        cur_tail[1] -= 1
                    case "L":
                        cur_tail[0] += 1
                    case "R":
                        cur_tail[0] -= 1
            head_visited.add(tuple(cur_head))
            tail_visited.add(tuple(cur_tail))
    return len(tail_visited)

print(tail_visits("example"))
print(tail_visits("input"))
