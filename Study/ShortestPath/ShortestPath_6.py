# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-


"""
미래도시 - Dijk
"""
import heapq

def dijk(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            new = dist+i[1]
            if new < distance[i[0]]:
                distance[i[0]]=new
                heapq.heappush(q,(new,i[0]))

n,m = list(map(int,input().split()))
INF=int(1e9)

distance=[INF] * (n+1)
graph=[[] for i in range(n+1)]

for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append((b,1))
    graph[b].append((a,1))

x,k = list(map(int,input().split()))



# First, graph[1][k]    
dijk(1)
FromOnetoK= distance[k]
#print(FromOnetoK)


#Initialize
distance=[INF] * (n+1)

# Second, graph[k][x]
dijk(k)
FromKtoX = distance[x]
#print(FromKtoX)

res=FromOnetoK+FromKtoX

if FromOnetoK==INF or FromKtoX==INF:
    print(-1)
else:
    print(res)
    
    
    
    
    
"""
The Problem is :
    이건 a->x + x->k 의 꺾이는 경로를 구하는 것.
    Dijkstra는 한번에 가는 것만 지원한다.
    뭐 Dijkstra를 2번 돌리면 될거같기는 함.
    
    Ya! Feel So Good!
"""