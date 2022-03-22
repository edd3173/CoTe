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
            