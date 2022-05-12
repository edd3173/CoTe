N=int(input())
nData=list(map(int,input().split()))
mySet = {}
for n in nData:
    if n not in mySet.keys():
        mySet[n]=1
    else:
        mySet[n]+=1
M=int(input())
mData=list(map(int,input().split()))

for m in mData:
    if mySet.get(m)==None:
        print(0,end=' ')
    else:
        print(mySet.get(m),end=' ')