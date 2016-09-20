def makeGen():
  list = range(3)
  for i in list:
    yield i*i

x=makeGen()
for i in x:
   print(i)

