graph = {'A':['C', 'B'], 'B':['E', 'D'], 'E':['F'], 'F':['G'], 'G':['H'], 'H':['D'], 'K':['H']}


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if vertex in graph.keys():
               queue.extend(set(graph[vertex]) - visited)
    return visited

print(bfs(graph, 'A'))

