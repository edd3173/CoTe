import sys
sys.setrecursionlimit(10**6)


def dfs(graph,start,visited):
    visited[start]=True
    #print(start)
    orders.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

N,M,R = map(int, input().split())
visited =[False] * (N+1)
graph = [[] for _ in range(N+1)]
orders=[]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

dfs(graph,R,visited)
#print(orders)

for i in range(1,N+1):
    if i in orders:
        print(orders.index(i)+1)
    else:
        print(0)