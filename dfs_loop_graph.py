graph = {'A': set(['B', 'C']),
 'B': set(['A', 'D', 'E']),
 'C': set(['A', 'F']),
 'D': set(['B']),
 'E': set(['B', 'F']),
 'F': set(['C', 'E'])
}


def dfs(graph, start):
    visited, stack = set(), [start]
    print("start with one node in stack: ", start)
    print("start with empty visited: ", visited)
    while stack:
        print("This is my stack(pre-pop): ", stack);
        vertex = stack.pop()
        print("This is my stack(post-pop: ", stack);
        print("This is my vertex: ", vertex);
        print("This is my visited: ", visited);
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
            print('    ');

    print("done");
    return visited

dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}

