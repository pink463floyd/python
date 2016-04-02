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

bstAdd(root, 7);
bstAdd(root, 5);
bstAdd(root, 9);
bstAdd(root, 1);
bstShow(root);
