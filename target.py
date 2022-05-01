import collections
from time import sleep


class Methods:
    def main(self):
        nodes = ("A", "B", "C", "D", "E", "F", "G")
        graph = {
        "A": {"B": 9, "C": 5, "D": 13},
        "B": {"A": 9, "E": 10, "D": 3},
        "C": {"A": 5, "F": 12},
        "D": {"B": 3, "E": 6, "G": 14},
        "E": {"B": 10, "D": 6, "G": 7},
        "G": {"E": 7, "F": 10, "D": 14},
        "F": {"G": 10, "C": 12},
    }
        print("Dijkstra")
        sleep(2)
        x = self.recursiveDijkstra(self, graph, [], "S")

    def recursiveDijkstra(self, graph):
        while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]


print(visited)
            return

    def recursiveDepthSearch(self,graph, visited, node):
        if node not in visited:
            visited.append(node)
            for near in graph[node]:
                self.recursiveDepthSearch(self,graph, visited, near)
                if near in visited:
                    break
                else:
                    visited.pop(node)
            return visited


x=Methods
x.main(x)

