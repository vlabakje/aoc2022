import itertools

class Valve:
    def __init__(self, line):
        parts = line.split(" ")
        self.name = parts[1]
        self.rate = int(parts[4][5:-1])
        self.nexthops = list(v.rstrip(",") for v in parts[9:])
        self.open = False
        self.paths = []

    def __str__(self):
        return f"<Valve name={self.name} rate={self.rate} valves={','.join(self.nexthops)} open={self.open}>"


def dijkstra_paths(valves, source):
    unvisited_nodes = set(valves.keys())
    shortest_path = dict((n, 2**32) for n in valves.keys())
    shortest_path[source] = 0
    previous_nodes = {}
    while len(unvisited_nodes):
        lowest = None
        for name in unvisited_nodes:
            if lowest == None or shortest_path[name] < shortest_path[lowest]:
                lowest = name
        #print(f"{len(unvisited_nodes)=} {lowest=} {shortest_path[lowest]=}")
        for neigh in valves[lowest].nexthops:
            path_len = shortest_path[lowest] + 1
            if path_len < shortest_path[neigh]:
                shortest_path[neigh] = path_len
                previous_nodes[neigh] = lowest
        unvisited_nodes.remove(lowest)
    for name, valve in valves.items():
        if name != source and not valve.open and valve.rate:
            path = [name]
            while previous_nodes[path[0]] != source:
                path.insert(0, previous_nodes[path[0]])
            yield tuple(path), valve.rate


def max_pressure(filename):
    valves = dict()
    with open(filename) as fileh:
        for line in fileh:
            valve = Valve(line.strip())
            valves[valve.name] = valve
    for name, valve in valves.items():
        valve.paths = list(dijkstra_paths(valves, name))
    def next_paths(source, current_path, opened_valves):
        for p, _ in valves[source].paths:
            if p[-1] in opened_valves:
                continue
            if (sum(len(cp) for cp in current_path) + len(current_path) + len(p)) > 30:
                continue
            yield from next_paths(p[-1], current_path + (p,), opened_valves + [p[-1]])
        yield current_path, opened_valves
    top = 0
    for path, opened_valves in next_paths("AA", tuple(), []):
        pressure = 0
        minutes = 0
        for p, v in zip(path, opened_valves):
            minutes += len(p) + 1
            if minutes > 26:
                break
            pressure += (26 - minutes) * valves[v].rate
        for path2, opened_valves2 in next_paths("AA", tuple(), opened_valves[:]):
            minutes = 0
            pressure2 = pressure
            for p2 in path2:
                minutes += len(p2) + 1
                if minutes > 26:
                    break
                pressure2 += (26 - minutes) * valves[p2[-1]].rate
            #print(f"{path=} {path2=} {opened_valves=} {pressure=}")
            top = max(top, pressure2)
        print(top)
        #print(f"{path=} {path2=} {opened_valves=} {pressure=}")
    return top

if __name__ == "__main__":
    #print(max_pressure("example"))
    print(max_pressure("input"))
