graphA = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}

graphB = {'A':['C', 'B'], 'B':['E', 'D'], 'E':['F'], 'F':['G'], 'G':['H'], 'H':['D'], 'K':['H']}

graph = {'A':['B', 'C', 'E'],
         'B':['D'],
         'C':['D'],
         'E':['D']}

def find_path(graph, start, end, path=[]):
        path = path + [start];
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                #print(path, newpath);
                if newpath:  
                    return newpath
        return None


def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            print(node);
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    print(newpath, newpaths, paths);
                    paths.append(newpath)
        return paths

def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        paths = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not paths or len(newpath) < len(paths):
                        paths = newpath
        return paths


print(find_path(graph, 'A', 'D'));
print("----");
print(find_all_paths(graph, 'A', 'D'));
print("----");
print(find_shortest_path(graph, 'A', 'D'));

