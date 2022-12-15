class Range():
    def __init__(self, start, end):
        self.occupied = []
        self.start = start
        self.end = end

    def occupy(self, start, end):
        start, end = max(start, self.start), min(end, self.end)
        if not self.occupied:
            self.occupied.append((start, end))
            return
        for i in range(len(self.occupied)):
            if self.occupied[i] != (start, end) and overlap(self.occupied[i], (start, end)):
                self.occupied[i] = (min(self.occupied[i][0], start), max(self.occupied[i][1], end))
                break
        else:
            self.occupied.append((start, end))
            return
        # we changed one of the occupied entries so they _might_ conflict with one another.
        start, end = self.occupied.pop(i)
        self.occupy(start, end)

    def covered(self):
        return len(self.occupied) == 1 and (self.start, self.end) == self.occupied[0]


def overlap(one, two):
    if one[0] > two[0]:  # always make 1 start first
        one, two = two, one
    return one[1] >= (two[0]-1)


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
        return (sensor[0]-offset, sensor[0]+offset)


def check_line(sensors_beacons, y, max_x):
    r = Range(0, max_x)
    for sensor, beacon in sensors_beacons:
        if s_e := y_positions_visible(sensor, beacon, y):
            r.occupy(s_e[0], s_e[1])
            if r.covered():
                return None
    return r.occupied


def free_spot(filename, max_coord):
    sensors_beacons = list((sensor, beacon) for sensor, beacon in sensor_beacon(filename))
    for y in range(max_coord+1):
        if c := check_line(sensors_beacons, y, max_coord):
            return y, c

def main(filename, max_coord):
    y, c = free_spot(filename, max_coord)
    return (c[0][1]+1) * 4000000 + y

if __name__ == "__main__":
    print(main("example", 20))
    print(main("input", 4000000))
