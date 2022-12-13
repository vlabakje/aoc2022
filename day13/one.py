def parse(text):
    list_stack = []
    current_list = None
    current_number = []
    for c in text:
        match c:
            case "[":
                if current_list is None:
                    current_list = list()
                else:
                    list_stack.append(current_list)
                    current_list.append(list())
                    current_list = current_list[-1]
            case "]":
                if current_number:
                    current_list.append(int("".join(current_number)))
                    current_number = []
                if list_stack:
                    current_list = list_stack.pop()
            case ",":
                if current_number:
                    current_list.append(int("".join(current_number)))
                    current_number = []
            case _:
                current_number.append(c)
    return current_list


def pairs(filename):
    with open(filename) as fileh:
        for p in fileh.read().strip().split("\n\n"):
            a, b = p.split("\n")
            yield parse(a), parse(b)


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    for i in range(len(a)):
        if i >= len(b):
            return -1
        c = compare(a[i], b[i])
        if c != 0:
            return c
    if len(a) == len(b):
        return 0
    return 1

def main(filename):
    for i, (a, b) in enumerate(pairs(filename), start=1):
        print(f"===={i}====")
        c = compare(a,b)
        print(f"{c=}")
        if c >= 0:
            yield i

if __name__ == "__main__":
    print(sum(main("example")))
    print(sum(main("input")))
