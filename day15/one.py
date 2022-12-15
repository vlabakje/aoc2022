
def sensor_beacon(filename):
    def getint(text):
        if text.endswith(","):
            text = text[:-1]
        return int(text.split("=")[1])
    with open(filename) as fileh:
        for line in fileh:
            sensor, beacon = line.strip().split(": ")
            yield tuple(map(getint, sensor.split(" ")[-2:])), tuple(map(getint, beacon.split(" ")[-2:]))

def y_positions_visible(sensor, beacon, y):
    distance = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
    y_distance = abs(y - sensor[1])
    # print(f"{sensor=}, {beacon=} {distance=} {y_distance=}")
    if y_distance < distance:
        offset = (distance - y_distance) 
        for i in range(sensor[0]-offset, sensor[0]+offset+1):
            yield i


def main(filename, y):
    seen = set()
    beacons_y = set()
    for sensor, beacon in sensor_beacon(filename):
        # distance = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        #print(f"{sensor=}, {beacon=} {distance=}")
        #print(",".join(map(str, y_positions_visible(sensor, beacon, y))))
        for visible in y_positions_visible(sensor, beacon, y):
            seen.add(visible)
        if beacon[1] == y:
            beacons_y.add(beacon[0])
    return len(seen - beacons_y)

if __name__ == "__main__":
    print(main("example", y=10))
    print(main("input", y=2000000))
