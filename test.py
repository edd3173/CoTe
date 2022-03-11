v,e = map(int,input().split())
edges=[]
parent = [-1] * (v+1)
def find_parent(parent,x):
  if parent[x] != x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

for _ in range(e):
  x,y,cost = map(int,input().split())
  edges.append((cost,x,y))

for i in range(1,v+1):
  parent[i]=i

costSum=0
edges.sort()

SelectedEdges=[]

for edge in edges:
  cost,x,y = edge
  if find_parent(parent,x) != find_parent(parent,y):
    costSum+=cost
    SelectedEdges.append(cost)
    union_parent(parent,x,y)

#print(SelectedEdges)

ans = sum(SelectedEdges) - max(SelectedEdges)
print(ans)