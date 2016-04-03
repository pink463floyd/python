#Given a graph, start, and end point, find a path
#https://www.python.org/doc/essays/graphs/

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}



def find_path(graph, start, end, path=[]):
        print '***', start, end, path
        print start, [start]
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

print(find_path(graph, 'A', 'D'))

