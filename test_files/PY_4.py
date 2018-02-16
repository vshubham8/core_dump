l=[1,2,3,4,5,6,7,8,9,10]
even_sum=0
odd_sum=0
even=[]
odd=[]
for i in l:
 if i%2==0:
  even.append(i)
  even_sum=even_sum+i
 else:
  odd.append(i)
  odd_sum=odd_sum+i
print 'even=',even,' odd=',odd
print 'even_sum=',even_sum,' odd_sum=',odd_sum
