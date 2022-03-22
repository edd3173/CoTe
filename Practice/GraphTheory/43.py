def getParent(parent,x):
    if x!=parent[x]:
        parent[x]=getParent(parent,parent[x])
    return parent[x]

def unionParent(parent,x,y):
    x=getParent(parent,x)
    y=getParent(parent,y)
    
    if x<y:
        parent[y]=x
    else:
        parent[x]=y    


N,M = map(int,input().split())
iCost=0
parent=[-1] * (N+1)
edges=[]

for i in range(N+1):
    parent[i]=i
    
for _ in range(M):
    x,y,cost = list(map(int,input().split()))
    edges.append((cost,x,y))
    iCost += cost
    
edges.sort()
fCost=0
for edge in edges:
    cost,x,y = edge
    if getParent(parent,x) != getParent(parent,y): # NOT parent[x] != parent[y]
        unionParent(parent,x,y)
        fCost+=cost

print(iCost-fCost) 



