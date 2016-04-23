G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']
}


def dfs(G, start):
    visited = set();
    stack=[start];
    while stack:
        v = stack.pop();
        print(v);
        visited.add(v)
        x = set(G[v]) - set(stack)
        stack.extend(x - visited)


dfs(G, 'A');
print("----");


def dfs_fast(G, start):
    stack=[start];
    stack_hash = {start:None};
    visited = set();
    while stack:
       v = stack.pop();
       del stack_hash[v]
       print(v);
       visited.add(v);
       #only add to stack if not visited and if not in stack.
       for x in G[v]:
         if x not in stack_hash: 
           if x not in visited:
              stack.append(x);
              stack_hash[x]=None;


dfs_fast(G, 'A')
