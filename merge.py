# Array A[] has the items to sort; array B[] is a work array.
def TopDownMergeSort(A, B, n):
    CopyArray(A, 0, n, B);           
    TopDownSplitMerge(B, 0, n, A);  

def TopDownSplitMerge(B, iBegin, iEnd, A):
    if(iEnd - iBegin < 2) :
        return;
    iMiddle = (iEnd + iBegin) / 2;             
    TopDownSplitMerge(A, iBegin,  iMiddle, B);
    TopDownSplitMerge(A, iMiddle,    iEnd, B); 
    TopDownMerge(B, iBegin, iMiddle, iEnd, A);

def TopDownMerge(A, iBegin, iMiddle, iEnd, B):
    i = iBegin 
    j = iMiddle
    
    k = iBegin
    while k < iEnd:
        if (i < iMiddle and (j >= iEnd or A[i] <= A[j])) :
            B[k] = A[i];
            i = i + 1;
        else :
            B[k] = A[j];
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
