"""
화성탐사
"""


import heapq

INF = int(1e9)

n=int(input())
distance = [[INF] * (n) for _ in range(n)]

graph=[]
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

move_set = [(+1,0),(-1,0),(0,+1),(0,-1)]

def dijk(x,y): # dist doesn't need to be 2d array. it is a value.
   q=[]
   heapq.heappush(q,(graph[x][y],x,y))
   distance[x][y]=graph[x][y] # NOT a ZERO
   
   while q:
       dist,px,py = heapq.heappop(q)
       
       if distance[px][py] < dist:
           continue
    
       for move in move_set:
           nx=px+move[0]; ny=py+move[1]
           if nx<0 or nx>=n or ny<0 or ny>=n:
               continue
           cost = dist + graph[nx][ny]
           if cost < distance[nx][ny]:
               distance[nx][ny]=cost
               heapq.heappush(q,(cost,nx,ny))
    
"""

def dijk(start):
       q=[]
   heapq.heappush(q,(0,start))
   distance[start]=0 
   
   while q:
       dist,now = heapq.heappop(q)
       if distance[now] < dist:
           continue
       for i in graph[now]:
           cost = dist + i[1]
           if cost < distance[i[0]]:
               distance[i[0]]=cost
               heapq.heappush(q,(cost,i[[0]]))
"""


               

dijk(0,0)               
"""
for i in range(0,n):
    for j in range(0,n):
        print(distance[i][j],end=' ')
    print()
"""
print(distance[n-1][n-1])