import collections
from time import sleep


class Methods:
    def main(self):
        graph = {
        "A": {"B":9,"C":5,"D":13},
        "B": {"A":9,"E":10,"D":3},
        "C": {"A":5,"F":12},
        "D": {"B":3,"E":6,"G":14},
        "E": {"B":10,"D":6,"G":7},
        "G": {"E":7,"F":10,"D":14},
        "F": {"G":10,"C":12},
    }
        print("Dijkstra")
        sleep(2)
        x=self.recursiveDepthSearch(self,graph,[],"S")
        x.reverse()
        print(x)
        print("===============")
        print("Backtracking:")
        sleep(1)
        x=self.recursiveBacktracking(self,graph,"S","A",[])
        x.reverse()
        print(x)
        print("===============")
        print("Busca por largura:")
        print(str(self.breadthSearch(self,graph,"A")))


    def recursiveDijkstra(self, graph,visited):

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

