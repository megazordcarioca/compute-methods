#breadth search

graphJar = [[]]
stack = []
vertexSize = 0
passed = 0
count = 0


def breadth_search(graph, vertex):
    stack = set()
    while True:
        vertex = queue.pop(0)
        if vertex not in passed:
            passed.add(vertex)
            stack.extend(graph[vertex] - passed)
        else:
            break
    return passed