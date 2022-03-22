"""
행성터널
"""

from itertools import combinations

def findParent(parent,x):
    if parent[x]!=x:
        parent[x]=findParent(parent,parent[x])
    return parent[x] # if you return x, it fails!

def unionParent(parent,x,y):
    x=findParent(parent,x)
    y=findParent(parent,y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y
"""

Nice try, but out of memory.


N=int(input())
parent = [-1] * N
Coords=[]

for i in range(N):
    x,y,z = map(int,input().split())
    Coords.append((i,x,y,z)) # i for identity number

for i in range(N):
    parent[i]=i

Edges=[]

twoCoords = combinations(Coords,2) # pick 2 from coords, 

for pair in twoCoords:
    p1,x1,y1,z1 = pair[0]
    p2,x2,y2,z2 = pair[1]
    cost = min(abs(x1-x2),abs(y1-y2),abs(z1-z2))
    Edges.append((cost,p1,p2)) # append idnumber


Edges.sort()
Ans=0
cnt=0
for edge in Edges:
    cost, id1, id2 = edge
    if findParent(parent,id1) != findParent(parent,id2):
        unionParent(parent,id1,id2)
    
        Ans+=cost
        cnt+=1   
        
print(Ans)

"""

N=int(input())
parent = [0] * (N+1)
edges=[]
result=0
for i in range(1,N+1):
    parent[i]=i
    
x=[]; y=[]; z=[]

for i in range(1,N+1):
    data = list(map(int,input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))
    
x.sort(); y.sort(); z.sort()

for i in range(N-1):
    # x&x+1 value diff, x id, x+1 id
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

edges.sort()

for edge in edges:
    cost,a,b = edge
    if findParent(parent,a) != findParent(parent,b):
        unionParent(parent,a,b)
        result+=cost
print(result)


"""
Keypoint 1 -> id value를 넣기. 여기서는 idx.
diff_x, diff_y, diff_z를 edges에 append해버리는거.
따로 계산해서 append해도 무관. 왜냐? 셋다 넣어버릴거거든.
따라서 3*N번 을 비교하면 N개를 비교할 수 있지.
답지 해설에 설명 잘되어있다.
"""