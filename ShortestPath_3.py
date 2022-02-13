# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-


"""
    Floyd-Warshal
"""


INF = int(1e9)

n=int(input())
m=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
            
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b]=c
    
for k in range(1,n+1): # iterate for graph[i][k]+graph[k][j]
    # graph[i][j]
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
            
            
print(n,m)

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
            
