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
        x = self.Dijkstra(self,nodes, graph)
        print(x)

    def Dijkstra(self,nodes,graph):
        unvisited = {node:None for node in nodes}
        visited = {}
        start = "A"
        currentDistance = 0
        unvisited[start]= currentDistance
        
        while True:
            for neighbour, distance in graph[start].items():
                if neighbour not in unvisited: 
                    continue
                newDistance = currentDistance + distance
                if unvisited[neighbour ] is None or unvisited[neighbour] > newDistance:
                    unvisited[neighbour] = newDistance
                    visited[start] = currentDistance
                    del unvisited[start]
                    if not unvisited: break
                    candidates = [node for node in unvisited.items() if node[1]]
                    start, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
            return visited


x=Methods
x.main(x)

