# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-


"""
Future City
"""


n,m = map(int,input().split())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for j in range(m):
    a,b = map(int,input().split()) # Get two vertices
    graph[a][b]=1 # They are connected with cost 1
    # UNDIRECTED GRAPH!
    graph[b][a]=1

x,k = map(int,input().split())


#Floyd-Warshall

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
            
res=graph[1][k]+graph[k][x]

if graph[1][k]==INF or graph[k][x]==INF:
    print(-1)
else:
    print(res)