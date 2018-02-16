s=raw_input('Enter string of length 10 having atleast 2 repeating elements: ')
l=len(s)
if l!=10:
 print 'length is less than 10, try again...'
 exit(0)
li=list(s)
tu=tuple(s)
se=set(s)
#print li
#print tu
#print se
li1=['a','b','c','d','e']
li2=[1,2,3,4,5]
temp=[]
k=0
for i in li1:
 temp.append(i)
 temp.append(li2[k])
 k+=1
print temp
d=dict()
k=0
for i in li1:
 d[i]=li2[k]
 k+=1
print d
