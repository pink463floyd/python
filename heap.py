import copy

def heapsort( aList ):
  # convert aList to heap
  length = len( aList ) - 1
  leastParent = length / 2
  #print(leastParent)
  for i in range ( leastParent, -1, -1 ):
    print "-------------------"
    print aList;
    print i, aList[i]
    moveDown( aList, i, length )

  print("SORT");
  #print(aList);
  # flatten heap into sorted array
  #for i in range ( length, 0, -1 ):
    #if aList[0] > aList[i]:
      #swap( aList, 0, i )
      #moveDown( aList, 0, i - 1 )


def moveDown( aList, first, last ):
  largest = 2 * first + 1
  print "%s first=%d last=%d largest=%d" % ("move down", first, last, largest);
  while largest <= last:
    print "%s largest=%d <= last=%d" % ("while", largest, last);
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
      print("+")
      largest += 1

    # right child is larger than parent
    if aList[largest] > aList[first]:
      print("-")
      swap( aList, largest, first )
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      print("!")
      return # force exit


def swap( A, x, y ):
  print("SWAP %d %d" % (x,y));
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

def pretty(A) :
   end = len(A);
   i = 1;
   p=0;

   while i<end:
     j=0; 
     while j<i :
       if (p<end) : 
          print("%s " % (A[p])),
       p=p+1;
       j=j+1;
     print(" ");
     i=2*i;

x = ['a', 'e', 'x', 'y', 'z', 'u', 'v'];
old = copy.copy(x);
heapsort(x);
print old;
pretty(old);
print x;
pretty(x);



