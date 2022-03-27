#Backtracking

graph1 = {
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

def recursiveBacktracking(graph, nodes, cnode, visited):
    cnode = visited if cnode is None else nodes
    if cnode not in visited:
        nodes = visited.append(nodes)
        for near in graph[cnode]:
            recursiveBacktracking(graph, near, cnode, visited)
            if near in visited:
                break
            else:
                visited.pop(nodes)
        return visited


visited = recursiveBacktracking(graph1,"S","A",[])
visited.reverse()
print(visited)