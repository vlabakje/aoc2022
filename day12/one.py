class Map():
    def __init__(self, filename):
        self.nodes = {}
        with open(filename) as fileh:
            for y, line in enumerate(fileh):
                for x, h in enumerate(line.strip()):
                    match h:
                        case 'S':
                            self.start = (x, y)
                            self.nodes[(x, y)] = 0
                        case 'E':
                            self.end = (x, y)
                            self.nodes[(x, y)] = ord('z') - ord('a')
                        case _:
                            self.nodes[(x, y)] = ord(h) - ord('a')

    def dijkstra(self):
        unvisited_nodes = set(self.nodes.keys()) | set([self.start, self.end])
        shortest_path = dict((n, 2**32) for n in self.nodes.keys())
        shortest_path[self.end] = 2**32
        shortest_path[self.start] = 0
        previous_nodes = {}
        while len(unvisited_nodes):
            lowest = tuple(self.end)
            for node in unvisited_nodes:
                if shortest_path[node] < shortest_path[lowest]:
                    lowest = node
            if lowest == self.end:
                break
            #print(f"{len(unvisited_nodes)=} {lowest=} {shortest_path[lowest]=}")
            #print(pretty(shortest_path))
            for neigh in self.neighbours(lowest):
                path_len = shortest_path[lowest] + 1
                if path_len < shortest_path[neigh]:
                    shortest_path[neigh] = path_len
                    previous_nodes[neigh] = lowest
            unvisited_nodes.remove(lowest)
        return shortest_path[self.end]

    def neighbours(self, node):
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx, ny = node[0]+dx, node[1]+dy
            if (nx, ny) in self.nodes:
                if self.nodes[(nx, ny)] <= (self.nodes[node] + 1):
                    yield (nx, ny)


def main(filename):
    m = Map(filename)
    return m.dijkstra()


print(main("example"))
print(main("input"))
