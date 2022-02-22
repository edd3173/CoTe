# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-


"""[message]

3 2 1
1 2 4
1 3 2

"""

import sys
import heapq


input=sys.stdin.readline

INF=int(1e9)
N,M,C = map(int,input().split())

graph=[[] for i in range(N+1)]
distance=[INF] * (N+1)

for i in range(M):
  a,b,c = map(int,input().split())
  #since this is directed graph,
  graph[a].append((b,c)) # Tuple (vertice,cost)


# 총 걸리는 시간? 최대값
# 연결된 adj? hmm...

def dijk(start):
  q=[]
  distance[start]=0
  heapq.heappush(q,(0,start))

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      new = dist + i[1]
      if new < distance[i[0]]:
        distance[i[0]]=new
        heapq.heappush(q,(new,i[0]))
  
# If infinity, not connected!
dijk(C)

Cnt=0
Max=0
#print(distance)
for i in range(1,N+1):
  if distance[i] != INF:
    Max=max(Max,distance[i]) # if() max 갱신... 보다 max()가 훨씬 더 좋은 방법!
    if distance[i] != 0: # Distance가 0인 경우도 있지.
      Cnt+=1

#print(str(Cnt)+' '+str(Max))
print(Cnt, Max)



