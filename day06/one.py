def read(filename):
    with open(filename) as fileh:
        return fileh.read().strip()

def start_marker(filename):
    msg = read(filename)
    for i in range(len(msg)-4):
        m = msg[i:i+4]
        if len(set(m)) == 4:
            return i+4

print(start_marker("input"))
