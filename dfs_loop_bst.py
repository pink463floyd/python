from collections import deque;

class Node(object):
  def __init__(self, v):
     self.v=v;
     self.L=None;
     self.R=None;

  def myPrint(self):
     print(self.v);

def dfs2(n):
 stack=[];
 current = n;
 flag = True;

 while flag == True:   
   if (current != None):
     while (current != None):
       stack.append(current);
       current=current.L;  
   else:
     if len(stack)>0:
        x=stack.pop();
        x.myPrint();
        current=x.R;
     else:
        flag = False;

def dfs(n):
  if n == None: return;
  dfs(n.L);
  n.myPrint();
  dfs(n.R);

root = Node(50);
root.L = Node(25);
root.R = Node(75);
root.L.L = Node(5);
root.L.R = Node(35);
root.R.L = Node(55);
root.R.R = Node(100);

dfs(root);
dfs2(root);

