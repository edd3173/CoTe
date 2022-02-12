import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# n-node_num, m-edge_num
n,m = list(map(int,input().split()))

start=int(input())

graph=[[]for i in range(n+1)]

visited=[False] * (n+1)

distance=[INF] * (n+1)

for _ in range(m):
    # from A to B, of cost C
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) # Tuple 형식이네???

"""
def heapsort(iterable):
    h=[]
    result=[]
    for val in iterable:
        heapq.heappush(h,val)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
"""

"""
def get_smallest_node():
    min_val=INF
    idx=0
    for i in range(1,n+1): #vertices: 1 ~ n, total n
        if distance[i] < min_val and not visited[i]: # visited[i]==0. different from 'not in!'
            min_val=distance[i]
            idx=i
    return idx
"""

         
def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start)) # cost, vertice
    
    while q:
        dist,now = heapq.heappop(q) # cost, vertice 
        if distance[now]<dist: # Need not to update. Visited.
            continue
        for i in graph[now]: #like bfs, find adj
            new=dist+i[1] # i:[vert,cost <-> opp of q
            if new < distance[i[0]]:
                distance[i[0]]=new
                heapq.heappush(q,(new,i[0])) # 값이 바뀌었으므로, 갱신을 위해 queue에 넣어야.
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])
                
