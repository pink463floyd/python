def count_bits(number):
  count = 0;
  i = 0;
  while i<32 :
   if (number & 1) == 1:
      count = count + 1;
   number = number >> 1;
   i=i+1;

  return count;


while True:
  number = input('enter number, I will say if its a power of 2:');
  bits=count_bits(number);
  print(bits);

