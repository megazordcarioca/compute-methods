import collections
from time import sleep


class Methods:
    def main(self):
        graph = {
        "A": ["B","E"],
        "B": ["A","C","F"],
        "C": ["B"],
        "E": ["A", "I"],
        "I": ["E","J","N"],
        "N": ["I"],
        "J": ["I","O"],
        "F": ["B","G"],
        "G": ["F","H","L"],
        "H": ["G","D"],
        "D": ["H"],
        "L": ["G","M"],
        "M": ["L", "Q"],
        "Q": ["M","P"],
        "P": ["Q","O","S"],
        "O": ["J","P","R"],
        "R": ["O"],
        "S": ["P"]
    }
        print("Busca profunda:")
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

    def breadthSearch(self, graph, root):
        visit, queue = set(),collections.deque([root])
        visit.add(root)
        while queue:
            vert = queue.popleft()
            print(("\0")+str(vert))
            for near in graph[vert]:
                if near not in visit:
                    queue.append(near)
                    visit.add(near)

    def recursiveBacktracking(self,graph, nodes, cnode, visited):
        cnode = visited if cnode is None else nodes
        if cnode not in visited:
            nodes = visited.append(nodes)
            for near in graph[cnode]:
                self.recursiveBacktracking(self,graph, near, cnode, visited)
                if near in visited:
                    break
                else:
                    visited.pop(nodes)
            return visited
        

x=Methods
x.main(x)

