from array import *
ar=array('i',[5,3,6,8,1,9,0,12,])
ar1=array('i',[13,11,11,14,18])
s=ar+ar1
for i in range(len(s)):
  for j in range(i+1,len(s)):
      if s[i]>s[j]:
          s[i],s[j]=s[j],s[i]
print(s)
