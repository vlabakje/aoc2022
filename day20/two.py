class Number:
    def __init__(self, value):
        self.value = value * 811589153

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.value}"

def mix(arrangement, n):
    i = arrangement.index(n)
    arrangement.remove(n)
    arrangement.insert((i+n.value)%(len(arrangement)), n)
    
def grove_coords(filename):
    with open(filename) as fileh:
        original = [Number(int(line.strip())) for line in fileh]
        zeroindex = [i for i, n in enumerate(original) if n.value == 0][0]
        #print(f"{zeroindex=} {original[zeroindex]=}")
        arrangement = original[:]
        #print(original, arrangement)
        for x in range(10):
            for i in range(len(original)):
                mix(arrangement, original[i])
                #print(f"{x=} {i=}={original[i].value}\t {', '.join(str(a) for a in arrangement)}")
        for grove in (1000, 2000, 3000):
            print(f"{grove=} {arrangement[(grove+zeroindex)%len(original)]=}")
            yield arrangement[(grove+arrangement.index(original[zeroindex]))%len(original)].value

print(sum(grove_coords("example")))
print(sum(grove_coords("input")))
