
def getParent(a,parent):
    if parent[a] != a:
        parent[a] = getParent(parent[a],parent)
    return parent[a]

def unionParent(a,b,parent):
    a = getParent(a,parent)
    b = getParent(b,parent)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m = map(int,input().split())
graph=[]
parent = [-1] * (n+1)
for _ in range(n):
    row =list(map(int,input().split()))
    graph.append(row)
plan = list(map(int,input().split()))
for i in range(1,n+1):
    parent[i]=i
# we can see if plans construct a tree. which means share same parent

# unionParent the connected points
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            unionParent(i+1,j+1,parent) # Be Careful!

# now check if plans share same parent
Flag=True
p = parent[plan[0]]
for ele in plan:
    if parent[ele] != p:
        Flag=False
        break

if Flag:
    print("Yes")
else:
    print("No")