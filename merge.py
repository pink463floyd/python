def merge(data, start, end, scratch):
  if start == end: return;
  mid = end + start / 2; 
  merge(data, start, mid, scratch);
  merge(data, mid, end, scratch);
  aggregate(start, mid, end, data, scratch);
  copy(scratch, data, start, end);
  
def aggregate(start, mid, end, data, scratch)
  i = start; j = mid; k = 0;

  if (i>=mid):
    scratch[k] = data[j];
    k=k+1; j=j+1;
    
  if (j>=end):
    scratch[j] = data[i];
    k=k+1; i=i+1;
  
  if (data[i] > [data[j]):
    scratch[k]=data[j];
    k=k+1; j=j+1;
  else:
    scratch[k]=data[i];
    k=k+1; i=i+1;
       0   1    2    3    4    5    6    7
data=['a','x', 'm', 'q', 'r', 't', 'u', 'b'];
merge(data,0,8,scratch)
 mid=4
 merge(data,0,4,scratch)
  mid=2
  merge(data,0,2,scratch)
   mid=1
   merge(data,0,1, scratch)




def copy(B, A, start, end)
  i = start;
  while i<end:
   A[i] = B[i];
   i=i+1;

data=['a','x', 'm', 'q', 'r', 't', 'u', 'b'];
scratch=[];
merge(data,0,8,scratch);
print(data);


