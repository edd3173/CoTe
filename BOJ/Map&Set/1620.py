N,M = map(int,input().split())
nameData={}
indexData={}
for i in range(N):
    name = input().strip()
    nameData[name]=(i+1)
    indexData[i+1]=name

ans=[]
for _ in range(M):
    mData=input().rstrip()
    #print(mData)
    if mData.isdigit():
        ans.append(indexData.get(int(mData)))
    else:
        ans.append(nameData.get(mData))

for e in ans:
    print(e)

#print(indexData)  
    
