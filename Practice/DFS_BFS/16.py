"""
연구소

맞왜틀?

"""

from itertools import combinations
from collections import deque


n,m = map(int,input().split())
wall_num = 3
graph = []
# Input info
for _ in range(n):
    graph.append(list(map(int, input().split())))

blanks=[]
walls=[]
viruses=[]
#visited = [[False]* m for _ in range(n)]
move_set = [(+1,0),(-1,0),(0,+1),(0,-1)]

# Get info
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            blanks.append((i,j))
        elif graph[i][j]==1:
            walls.append((i,j))
        elif graph[i][j]==2:
            viruses.append((i,j))

def restoreMap(graph):
    for i in range(n):
        for j in range(m):
            if (i,j) in blanks:
                graph[i][j]=0
            elif (i,j) in walls:
                graph[i][j]=1
            elif (i,j) in viruses:
                graph[i][j]=2


def bfs(x,y): # starts in pos(x ,y)
    q=deque([(x,y)])
    #graph[x][y]=2 # just like 'mark as visited'
    #visited[x][y] = True # meaningless
    
    while q:
        now = q.popleft()
        px=now[0]; py=now[1]
        
        # for 4 direction:
        for move in move_set:
            nx = px + move[0]
            ny = py + move[1]
            
            # Invalid area, or already visited(means virus there) or there is a wall.
            if nx<0 or nx>=n or ny<0 or ny>=m or graph[nx][ny]==1 or graph[nx][ny]==2:
                continue
            
            # graph[nx][ny]=0 : Air
            graph[nx][ny]=2 
            q.append((nx,ny))
            
            # NEED NOT TO UPDATE? since this is not a recursive
            #px=nx ; py=ny; # Is updating here right? Nope
            # px와 py가 변하면, 절대 안되지! nx와 ny가 한단계 더 깊어지니까!
        


# Select 3 spots from blank, set wall
possibleWalls = combinations(blanks,wall_num)

ans=-1
cnt=0

# for possible Walls, let's see how virus expands. we can do this by bfs (and dfs, too)
for chosenWalls in possibleWalls: # chosen Walls
    
    #print(chosenWalls)
    
    # Modify graph of new walls
    for newWall in chosenWalls:
        graph[newWall[0]][newWall[1]]=1
    
    # do some bfs to virsues, changing infected areas
    for virus in viruses:
        bfs(virus[0],virus[1])


    # Check how many 0s survivied after bfs
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                cnt+=1
    
    #print(cnt)
    ans=max(ans,cnt) # find maximum safe area
    
    #restore map
    restoreMap(graph)
    cnt=0

print(ans)