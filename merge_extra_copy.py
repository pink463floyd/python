def mrg(a, start, end):
  print(start, end)
  if start == end:
     return 

  mid = (start+end)//2

  mrg(a, start, mid);
  mrg(a, mid+1, end)
  cat2(a, start, mid, end)

def cat2(a, start, mid, end):
  print("merge %d-%d with %d-%d" % (start, mid, mid+1, end))
  tmp=[];
  for x in a:
    tmp.append(x)
  cat3(tmp, a, start, mid, end);
  

def cat3(source, dest, start, mid, end):
 i = start;
 k = start;
 j = mid+1
 while i <= mid and j <=end:
  if source[i] < source[j]:
   dest[k] = source[i];
   i = i+1
  else :
   dest[k] = source[j];
   j = j+1
  k = k+1

 while i <=mid :
   dest[k] = source[i];
   i = i + 1 
   k = k+1

 while j <=end :
   dest[k] = source[j];
   j = j + 1 
   k = k+1
   

a=['z', 'x', 'y', 't', 'w', 'v', 'u', 'm'];
mrg(a, 0, 7)
print(a);
