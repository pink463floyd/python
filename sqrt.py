

def ssqrt(x) :
   right = x;
   left = 1;
   result=0

   while left<=right :

      mid = (left+right) /2 ;

      if mid <= x/mid:
       
         left=mid+1;
         print("set result %d" % (mid));

         result=mid;

      else:

         right = mid-1;

      print "%d %d %d %d %d" % (left, right, mid, x/mid, result)

   return result;


print ssqrt(8);
