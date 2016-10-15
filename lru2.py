import collections

class lru(object) :
    def __init__(self, max) :
       self.d = collections.OrderedDict()
       self.max = max;

    def p(self) :
      print self.d

    def get(self, k) :
       try:
         v = self.d.pop(k); 
         self.d[k]=v;
         #self.put(k,v);
  
       except KeyError:
         v = -1

       return v;
  

    def put(self, k,v) : 
       try:
         '''Are we updating incumbent key'''
         v2 = self.d.pop(k); 
         self.d[k]=v;

       except KeyError:
         '''Since we are here, key not present'''
         '''first step is to see if cache is full'''
         if len(self.d) >= self.max :
            self.d.popitem(last=False)
           
         '''Assert thyself!'''
         self.d[k]=v;


x=lru(3)
#print x.get("janet")
x.put("ethan", 12)
x.put("janet", 53)
x.put("scott", 54)
x.put("dad", 74)
#x.p()
#print x.get("ethan")
x.p()
