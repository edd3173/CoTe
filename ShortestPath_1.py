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

def get_smallest_node():
    min_val=INF
    idx=0
    for i in range(1,n+1): #vertices: 1 ~ n, total n
        if distance[i] < min_val and not visited[i]: # visited[i]==0. different from 'not in!'
            min_val=distance[i]
            idx=i
    return idx
            
def dijkstra(start):
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1] # j[0]:Vertice, j[1]:Cost_of_edge
    
    for i in range(n-1): #  here, we iterate all 2~n, so total n-1 times
        now = get_smallest_node()
        visited[now]=True
        for j in graph[now]: # For Current visited node, find adj vertices
            new = distance[now]+j[1] # cost to reach now + from now to adj vertices
            if new < distance[j[0]]: # Original Value in dist[], cost from start to j : dist[j[0]]
                distance[j[0]]=new
                
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])
                