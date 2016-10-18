# Array src[] has the items to sort; array scratch[] is a work array.
def TopDownMergeSort(src, scratch, n):
    CopyArray(src, 0, n, scratch);           
    TopDownSplitMerge(scratch, 0, n, src);  

def TopDownSplitMerge(scratch, iBegin, iEnd, src):
    if(iEnd - iBegin < 2) :
        return;
    iMiddle = (iEnd + iBegin) / 2;             
    TopDownSplitMerge(src, iBegin,  iMiddle, scratch);
    TopDownSplitMerge(src, iMiddle,    iEnd, scratch); 
    TopDownMerge(src, iBegin, iMiddle, iEnd, scratch);

def TopDownMerge(src, iBegin, iMiddle, iEnd, scratch):
    i = iBegin 
    j = iMiddle
    
    k = iBegin
    while k < iEnd:
        if (i < iMiddle and (j >= iEnd or scratch[i] <= scratch[j])) :
            src[k] = scratch[i];
            i = i + 1;
        else :
            src[k] = scratch[j];
            j = j + 1;    
        k = k + 1

def CopyArray(A, iBegin, iEnd, B):
    k = iBegin
    while k < iEnd:
        B.append(A[k]);
        k=k+1

A=['x', 'z', 'a', 'b', 'r', 'n', 'm', 'l']
B=[]
TopDownMergeSort(A, B, 7)
print A
