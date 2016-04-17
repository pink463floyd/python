S=set()

def add(ordinal):
  if ordinal not in S:
     print("This is a new number, I will remember it");
     S.add(ordinal)
  else:
     print("Sigh, repeating oneself is so boring");


while True:
  ordinal = input('enter number:');
  add(ordinal);



