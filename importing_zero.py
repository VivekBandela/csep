from array import *
a=array('i',[1,0,2,3,0,4,5,0,8,9,0])
print("before update:",a)
i=0
w=len(a)
c=0
for i in a:
  if i==0:
     c=c+1
s=w+c
while i<s:
 if a[i]==0:
    a.insert((i+1),0)
    i=i+2
 else:
    i=i+1
print("updated array:",a)
