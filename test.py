import heapq

n,m = map(int,input().split())
INF=int(1e9)
distance=[INF] * (n+1)
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijk(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijk(1)
print(distance)

maxVal=-1; maxNode=-1; cnt=0

maxVal = max(distance[1:])
maxNode = distance.index(maxVal)
cnt = distance.count(maxVal)


print(maxNode,maxVal,cnt)