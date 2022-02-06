""" Maze Escape """

from collections import deque

n,m = list(map(int,input().split()))
graph=[]
dx=[1,-1,0,0]
dy=[0,0,+1,-1]

for i in range(n):
  graph.append(list(map(int,input())))

#print(n,m)
#print(graph)
ans=0

def bfs(x,y): # Is visited necessary? Nope!
  global ans
  Queue=deque([(x,y)]) # Tuple Insert 
  #or, queue.append((x,y))

  #graph[x][y]=0 # To Mark Visited 필요없네. 노드의 값을 올려주는 로직.
  print(Queue)
  print( '('+str(x)+','+str(y)+')') # Print Current

  while Queue: # When to ans++?
    """
    iteration마다 ans++를 때리는게 아니라, 노드의 값을 바꾼다!
    """
    ct=Queue.popleft()
    #print(type (ct))
    px=ct[0]; py=ct[1] # Tuple access

    # Or, x,y = queue.popleft()


    if px== n-1 and py== m-1:
      print(graph[px][py])
      break
    print( '('+str(px)+','+str(py)+')')
    for i in range(4):
      nx=px+dx[i]; ny=py+dy[i];
      if(nx<0 or nx>=n or ny<0 or ny>=m or graph[nx][ny] == 0):
        #continue? what to do?
        #nx-=dx[i]; ny-=dy[i] # Go back
        continue
        """
        Continue 때려도 되네. why? loop 돌면 기존 nx는 어차피 무관.
        새로 nx=pd+dx[i]로 바뀌니까. 
        """

      #else:
      # 처음 방문하는 경우에만!
      if graph[nx][ny]==1:
        Queue.append((nx,ny)) # Tuple append
        graph[nx][ny]=graph[px][py]+1 # New=Old+1

bfs(0,0)

#print(ans)



