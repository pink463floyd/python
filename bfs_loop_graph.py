from collections import deque;

G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E', 'A']
}

def bfs(g, start):
    visited = set();
    q=deque([start]);
    while q:
        vertex = q.popleft()
        print(vertex);
        visited.add(vertex)
        x=set(g[vertex])-set(q);
        q.extend(x - visited);

bfs(G, 'A');
