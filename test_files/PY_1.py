name="Ilovepython"
print "Length:",len(name)
name=name+"Ilovepython"
print len(name)
no=int(raw_input())
name=name+5*str(no)
print name
l=len(name)
li=[]
s=""
for i in range(0,l):
 if i%2 == 0:
  li.append(name[i])
  s=s+name[i]
print li
s=s[::-1]#technique to reverse string
print s
ll=len(s)
temp=""
for i in range(0,ll):
 if s[i]>='0' and s[i]<='9':
  temp=temp+'a'
 else:
  temp=temp+s[i]
print temp
print temp.upper()
