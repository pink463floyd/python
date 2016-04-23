G={'A':['B', 'C', 'D'],
   'B':['A', 'E'],
   'C':['A', 'F'],
   'D':['A', 'G'],
   'E':['B'],
   'F':['C'],
   'G':['D']}


def dfs2(G, n, visited=None):
   if visited == None:
      visited = set();
   print(n);  
   visited.add(n);
   for x in set(G[n]) - visited:
    dfs2(G, x, visited);

dfs2(G, 'B');


graph = {'A': set(['B', 'C']),
 'B': set(['A', 'D', 'E']),
 'C': set(['A', 'F']),
 'D': set(['B']),
 'E': set(['B', 'F']),
 'F': set(['C', 'E'])
}

def dfs(graph, start, visited=None):
    print(start, visited);
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}




class Node(object):
  def __init__(self, v):
     self.v=v;
     self.list=[];

  def myPrint(self):
     print(self.v);

  def add(self, n):
     self.list.append(n);

  def __eq__(self, other): 
        return self.__dict__ == other.__dict__
        #return self.v == other.v

  def __str__(self, other): 
        return self.__dict__ == other.__dict__
        #return self.v == other.v


def dfs3(n, visited=None):
    n.myPrint();
    if visited is None:
        visited = set()
    visited.add(n)
    print("----");
    print(visited);
    #print(n.list);
    #for i in (set(n.list) - visited):
       #print(i);
    print("----");
    for next in (set(n.list) - visited):
        dfs3(next, visited)


a = Node('A');
b = Node('B');
c = Node('C');
d = Node('D');
e = Node('E');
f = Node('F');
g = Node('G');

a.add(b);
a.add(c);
b.add(a);
b.add(d);
b.add(e);
c.add(a);
c.add(f);
d.add(b);
e.add(b);
e.add(f);
f.add(e);
f.add(c);
dfs3(b);

