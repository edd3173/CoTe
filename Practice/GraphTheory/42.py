def getParent(parent,x):
    if parent[x] != x:
        x=getParent(parent,parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a=getParent(parent,a)
    b=getParent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

"""
logic을 완벽히 이해한건 아님
"""
G=int(input())
P=int(input())
arr=[]
for _ in range(P):
    arr.append(int(input()))
#print(arr)
parent = [-1] * (G+1)

for i in range(G):
    parent[i]=i

for ele in arr: # for each element in arr
    Flag=False
    for i in range(1,ele+1): # try to dock from left
        if parent[i] != 0: # if not docked
            unionParent(parent,i,i-1)
            continue
            
            
"""
myCode

def findParent(parent,x):
    if parent[x]!=x:
        return findParent(parent,parent[x])
    return parent[x]

def unionParent(parent,x,y):
    x=findParent(parent,x)
    y=findParent(parent,y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y


G=int(input())
P=int(input())
arr=[]
for _ in range(P):
    arr.append(int(input()))
    
parent = [0] * (G+1)
for i in range(1,G+1):
    parent[i]=i

ans=0
for a in arr:
    if findParent(parent,a) !=0:
       print("docking a",a,"with no probl!")
       unionParent(parent,0,a)
       ans+=1
    else:
        print("docking a",a,"is on prob! going deeper")
        myFlag=True # am I fucked?
        for i in range(a-1,0,-1): # for smaller dockers
            res = findParent(parent,i) # find parent
            if res !=0: # if docking available,
                unionParent(parent,0,i) # dock
                ans+=1
                myFlag=False # phew!
        if myFlag==True: # ah shit
            print("Exit, since we got problem with:",a)
            break

print("ans:",ans)

"""