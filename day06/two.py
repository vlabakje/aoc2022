def read(filename):
    with open(filename) as fileh:
        return fileh.read().strip()

def start_marker(filename):
    msg = read(filename)
    for i in range(len(msg)-14):
        m = msg[i:i+14]
        if len(set(m)) == 14:
            return i+14

print(start_marker("input"))
