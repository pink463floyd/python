G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']
}


def dfs(G, start):
    visited = set();
    stack=[];
    stack.append(start);
    while stack:
        v = stack.pop()
        print(v);
        visited.add(v)
        x = set(G[v]) - set(stack)
        stack.extend(x - visited)
        #stack.extend(set(G[v]) - visited)


dfs(G, 'A') 

