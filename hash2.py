tbl = [];
#myMod = 127;
myMod = 7;
''' 'aaa' and 'hhh' and 'ooo' hash to same value '''
class node(object):
  def __init__(self, foo) :
      self.collision_list = [];
      self.value = foo;

  def __str__(self) :
      return self.value;


def myHash(str) :
    hashValue = 0;
    position = 10;
    for j in str :
      hashValue = hashValue + (ord(j) * position);
      position = position * 10;
    return hashValue % myMod;

def dump() :
   j=0;
   for i in range(myMod) :
      #print("%d: %s" % (i, tbl[i]));
      print(tbl[i]);
      if tbl[i] != None: 
         print(tbl[i].collision_list);

for i in range(myMod) :
   tbl.append(None);

def add(str) :
  #str = input('enter value to be hashed: ');
  hashValue = myHash(str);
  if tbl[hashValue] == None:
     print("native");
     tbl[hashValue] = node(str);  
  else :
     print("overflow");
     tbl[hashValue].collision_list.append(str);
  print hashValue;


def find(str) :
  hashValue = myHash(str);
  if tbl[hashValue] != None:
     print(tbl[hashValue], str);
     if tbl[hashValue].value == str :
        return "Found in table";
     else:
        for i in tbl[hashValue].collision_list:
           print(i, str);
           if i == str :
              print("Found in overflow list");
              return;

  print("Not found!");
  return;
