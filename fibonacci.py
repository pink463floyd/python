while True:
  fibList = [0,1];
  fibLen = input('enter length of fibonacci sequence:');
  i=2;
  while (i < fibLen):
    fibList.append(fibList[len(fibList)-1] + fibList[len(fibList)-2]);
    i=i+1;
  print(fibList);
