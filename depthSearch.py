#Busca profunda

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

def recursiveDepthSearch(graph, visited, node):
    if node not in visited:
        visited.append(node)
        for near in graph[node]:
            recursiveDepthSearch(graph, visited, near)
            if near in visited:
                break
            else:
                visited.pop(node)
        return visited


visited = recursiveDepthSearch(graph1, [] ,"S")
visited.reverse()
print(visited)