def foo(loner):
  j=0;
  for person in table:
     print person[loner];
     if person[loner] == 0:
        if j!=loner:
           print("there is no influencer, an inflencer is followed by everyone but himself");
           return;
     j=j+1;
  print(" %d really is our influencer" % (loner));

person0=[0,1,1,1];
person1=[1,0,1,0];
person2=[0,0,0,0];
person3=[0,0,1,1];
table=[person0, person1, person2, person3];

for person in table:
   print person;

print("beg - list of loners:");
i = 0;
for person in table:
  if 1 not in person:
    print("person %d has no friends" % (i));
  i=i+1;
print("end - list of loners:");


i = 0;
loner=-1;
for person in table:
  if 1 not in person:
    loner=i;
    break;
  i=i+1;
print("stored loner in 'loner' variable: ", loner);

foo(loner);
