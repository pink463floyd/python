x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def bs(data, i):
   start = 0;
   end = len(data)-1;
   found = False;

   while start<=end and not found:
     mid = (start+end)//2;

     if data[mid] == i:
        found = True;
     else:
        if i < data[mid]:
           end = mid-1;
        else:
           start=mid+1;
   
   print(mid, start, end);
   if found:
     return mid;
   else:
     return -1;


print(bs(x,15));
