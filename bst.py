class Node(object):
    def __init__(self, key_value):
        self.left = None;
        self.right = None;
        self.key = key_value;

    def display(self):
        print self.key;

root = Node(None);

def bstAdd(node, key):
#check for empty tree
   if node.key == None:
      node.key = key;
      return;

   if key < node.key:
     if node.left == None:
       node.left = Node(key);
     else:
       bstAdd(node.left, key)
   else:
     if node.right == None:
       node.right = Node(key);
     else:
       bstAdd(node.right, key)

def bstShow(node):
   if node == None:
      return;

   bstShow(node.left);
   node.display()
   bstShow(node.right);

#Do a breadth first traversal
def breadth(node):
   curList = [];
   nextList = [];

   curList.append(node);
   displayList = [];
   while (len(curList) > 0):
     for x in curList:
       displayList.append(x.key);
       if (x.left != None) :
          nextList.append(x.left);
       if (x.right != None) :
          nextList.append(x.right);
     print(displayList);
     displayList=[];
     curList = [];
     curList = list(nextList);
     nextList=[];
   
bstAdd(root, 10);
bstAdd(root, 5);
bstAdd(root, 15);
bstAdd(root, 2);
bstAdd(root, 8);
bstAdd(root, 12);
bstAdd(root, 18);
bstShow(root);
print("Breadth traversal");
breadth(root);
