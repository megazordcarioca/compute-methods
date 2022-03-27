#breadth search

graph1 = {                          #Labirinto
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

from pydoc import resolve
import queue
import collections

def breadthSearch(graph, root):
    visit, queue = set(),collections.deque([root])
    visit.add(root)
    while queue:
        vert = queue.popleft()
        print(("\0")+str(vert))
        for near in graph[vert]:
            if near not in visit:
                queue.append(near)
                visit.add(near)


x = breadthSearch(graph1, "A")
print(x)





