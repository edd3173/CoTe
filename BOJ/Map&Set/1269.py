N,M = map(int,input().split())
nData=set(list(map(int,input().split())))
mData=set(list(map(int,input().split())))

nMinus = nData - mData
mMinus = mData - nData
ansSet = nMinus | mMinus

#print(ansSet)
print(len(ansSet))