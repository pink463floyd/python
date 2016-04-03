def quick(data, start, end):
   if (start >= end):
      return;
   mark = partition(data, start, end);
   quick(data, start, mark);
   quick(data, mark+1, end);

def partition(data, start, end):
   pivot=data[end-1];
   i=start;
   j=start;

   while(i<(end-1)):
     if data[i] <= pivot:
        swap(data,i,j);
        j=j+1;
     i=i+1;
   swap(data, j, end-1);
   return j;

def swap(data, a, b):
   tmp=data[a];
   data[a]=data[b];
   data[b]=tmp;

data=['a','x', 'm', 'q', 'r', 't', 'u', 'b'];
quick(data,0,8);
print(data);
