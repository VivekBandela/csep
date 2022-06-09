from array import *
ar=array('i',[1,0,2,3,0,4,5,0])
print("before updated:",ar)
l=[]
for i in ar:
 l.append(i)
 if i==0:
   l.append(0)
print("updated array:",l)
