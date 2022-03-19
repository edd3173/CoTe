"""
숨바꼭질
with dijk
"""

"""
import heapq
INF = int(1e9)
N,M = map(int,input().split())
distance = [INF] * (N+1)
graph=[[] for _ in range(N+1)]

for _ in range(M):
    src,dst = map(int,input().split())
    graph[src].append((dst,1)) # since cost is set to 1
    graph[dst].append((src,1))

def dijk(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijk(1)
print(distance)
distance[0]=-1
cnt=0
maxVal = max(distance)
maxIdx = distance.index(maxVal)
for d in distance:
    if d == maxVal: cnt+=1

print(maxIdx,maxVal,cnt)
"""

from collections import deque
INF = int(1e9)
N,M = map(int,input().split())
distance = [INF] * (N+1)
graph=[[] for _ in range(N+1)]

for _ in range(M):
    src,dst = map(int,input().split())
    graph[src].append(dst) # since cost is set to 1
    graph[dst].append(src)

def bfs(start):
    q=deque([start])
    distance[start]=0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == INF:
                distance[i]=distance[now]+1
                q.append(i)

bfs(1)
print(distance)
distance[0]=-1
cnt=0
maxVal = max(distance)
maxIdx = distance.index(maxVal)
for d in distance:
    if d == maxVal: cnt+=1

print(maxIdx,maxVal,cnt)