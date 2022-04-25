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

n,m = map(int,input().split())
graph=[];
for _ in range(n):
    graph.append(list(map(int,input().split())))
path = list(map(int,input().split()))
parent = [-1] * (n+1)
for i in range(1,n+1):
    parent[i]=i

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
           unionParent(parent,i+1,j+1)

res = []
for p in path:
    res.append(parent[p])
print(res)

if res.count(res[0])==len(res):
    print("Yes")
else:
    print("No")