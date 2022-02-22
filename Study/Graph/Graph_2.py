from collections import deque


"""
Added BFS answer code.
"""


n,m = map(int,input().split())
move_set=[(0,+1),(0,-1),(+1,0),(-1,0)]
graph=[]
#cnt=0
for _ in range(n):
  graph.append(list(map(int,input())))

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

def bfs(px,py):
  if graph[px][py] == 1:
    #print("Wrong Input!")
    return False

  q=deque([(px,py)])
  graph[px][py]=1 # mark visited
  print("(%d, %d)",px,py)
  while q:
    v = q.popleft()
    px=v[0]; py=v[1]
    for move in move_set:
      nx=px+move[0]; ny=py+move[1]
      if nx<0 or nx>=n or ny<0 or ny>=m :
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny]=1
        q.append((nx,ny))
  return True
    
cnt=0
for i in range(n):
  for j in range(m):
    if bfs(i,j)==True: cnt+=1

print(cnt)



      
    


"""
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True: cnt+=1
"""

    
