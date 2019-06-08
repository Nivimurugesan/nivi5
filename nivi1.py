x1,x2=input().split()
temp=0
if len(x1)>len(x2):
  x1,x2=x2,x1
i=0
while i<len(x1):
  temp+=(ord(x2[i])-ord(x1[i]))
  i+=1
for i in range(i,len(x2)):
  temp+=ord(x2[i])-ord('a')+1
print(temp)
