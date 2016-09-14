#Lowest Common Ancestor
class Node(object) :


 def __init__(self, value):
    self.L=None;
    self.R=None;
    self.V=value;

 def myPrint(self) :
    print(self.V);


tree = Node(100);
tree.L = Node(50);
tree.L.L = Node(25);
tree.L.R = Node(75);
tree.R = Node(150);
tree.R.R = Node(200);
tree.R.L = Node(125);
'''          100
       50          150
    25    75    125   200
'''

def lca(t, a, b) :

   ret = t.V;
   if a < t.V and b < t.V :
      ret = lca(t.L, a, b);
   else:
      if a > t.V and b > t.V :
         ret = lca(t.R, a, b);

   return ret; 
 



print lca(tree, 25, 75);
print lca(tree, 25, 200);
