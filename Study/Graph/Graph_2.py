from collections import deque


"""
Added BFS answer code.
"""


"""
def dfs(px,py):
  if px<0 or px>=n or py<0 or py>=m: # blocked
    return False
  if graph[px][py]==0: # land, or unvisited
    graph[px][py]=1 # mark visited (by changing land to water)
    dfs(px+1,py)
    dfs(px-1,py)
    dfs(px,py+1)
    dfs(px,py-1)
    return True # Last visit in chunk, return true
  return False
"""

from collections import deque

n,m = map(int,input().split())
arr=[]
for _ in range(n):
  arr.append(list(map(int,input())))

move_set = [(+1,0),(-1,0),(0,+1),(0,-1)]

def bfs(x,y):
  if arr[x][y]==1: # 바로 여기서!
    return False
  
  q=deque([(x,y)])
  arr[x][y]=1 # mark as visited
  
  while q:
    px,py = q.popleft()
    for move in move_set:
      px += move[0]; py +=move[1]
      if 0<=px<n and 0<=py<m and arr[px][py]==0: 
        arr[px][py]=1 # mark as visited
        q.append((px,py))
  return True # 그럼 return false는 언제해???
  
cnt=0
for i in range(n):
  for j in range(m):
    res = bfs(i,j)
    if res == True:
      cnt+=1

print(cnt)


      
    


"""
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True: cnt+=1
"""

    
