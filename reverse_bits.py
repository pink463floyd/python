def rev(n) :

 hb = 0
 out = 0
 i=1

 while i<=64:
  if n & 0x8000000000000000 :
   out = out + (1<<i)
  n = n << 1
  i = i+1

 return out; 
