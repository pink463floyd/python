import sys

def count_char(str):
  dict = {};

  str=str.replace(" ", "");
  str=str.lower();


  for x in str:
     if x in dict.keys():
      dict[x]=dict[x]+1;
     else:
      dict[x]=1;
  print(dict);


if (sys.version_info[0]<3):
  print("Please run with python 3.x");
  exit(0);



while True:
  str = input('enter string:');
  count_char(str);

