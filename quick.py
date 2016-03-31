def swap(A, a, b):
        print(a, b)
        tmp = A[a];
        A[a] = A[b];
        A[b] = tmp;
    
def partition(A, lo, hi) :
   piv = A[hi];
   j = lo;
   i = lo;
   while j < (hi)  :
     print j, hi, hi-1;
     if A[j] <= piv :
        swap(A, i, j);
        i = i + 1;
     j = j + 1;
   swap(A, i, hi); 
   return i;

arr=[9,6,4,3,2,1,5];
partition(arr, 0, 6);
print(arr);

