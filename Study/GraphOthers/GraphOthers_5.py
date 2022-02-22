
"""
도시분할계획
"""

def find_parent(parent,x):
    if x != parent[x]:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

"""
Kruskal algorithm을 완벽하게 모른다!
graph가 아니라 edges! 데이터 입력받는 법!
그리고 parent[i]=i까지.
"""

n,m = map(int,input().split())
#graph = [[]* (n+1) for _ in range(n+1)]
#graph = [] NOT graph, but EDGES!
parent = [0] * (n+1)
for i in range(n+1):
    parent[i]=i
edges=[]

for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
edges.sort()

max_cost = 0
ans=0

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans+=cost; max_cost=max(max_cost,cost)

print(ans-max_cost)
        



    
    