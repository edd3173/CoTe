
def find_parent(parent,x):
  if x!=parent[x]:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b
  
n,m = map(int,input().split())
parent=[0] * (n+1)

for i in range(1,n+1):
  parent[i]=i

for _ in range(m):
  x,a,b =map(int,input().split())
  if x==0:
    union_parent(parent, a, b)
  elif x==1:
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if pa == pb:
      print("YES")
    else:
      print("NO")

  