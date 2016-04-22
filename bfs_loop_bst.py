from collections import deque;

class Node(object):
  def __init__(self, v):
     self.v=v;
     self.L=None;
     self.R=None;

  def myPrint(self):
     print(self.v);

def bfs(n):
 q=deque([]);
 current = n;
 flag = True;

 q.append(n);
 while len(q) > 0:
   x=q.popleft();
   x.myPrint();
   if x.L != None: q.append(x.L);
   if x.R != None: q.append(x.R);

root = Node(50);
root.L = Node(25);
root.R = Node(75);
root.L.L = Node(5);
root.L.R = Node(35);
root.R.L = Node(55);
root.R.R = Node(100);

bfs(root);

