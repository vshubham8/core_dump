t=int(raw_input())
while(t):
    word=raw_input()
    l1=len(word)
    count=0
    for i in xrange(0,l1-1):
        for j in xrange(i+1,l1):
            temp=list(word[i:j+1])
            tempr=temp[::-1]
            if temp==tempr:
                count=count + pow(len(temp),2)
    count+=l1
    print count
    t-=1