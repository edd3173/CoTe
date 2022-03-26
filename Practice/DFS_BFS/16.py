from collections import deque
from itertools import combinations

N,M = map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

moveSet = [(+1,0),(-1,0),(0,+1),(0,-1)]
viruses=[]
walls=[]
blanks=[]

def myBFS(px,py):
    q=deque([(px,py)])
    while q:
        now = q.popleft()
        px,py = now # 와 이게 빠져서 틀렸었네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        for move in moveSet:
            nx=px+move[0]; ny=py+move[1]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0: # only available place to infect
                graph[nx][ny]=2 # infect
                q.append((nx,ny))
            else:
                continue

def restoreGraph(myGraph):
    for i in range(N):
        for j in range(M):
            if (i,j) in viruses:
                myGraph[i][j]=2
            elif (i,j) in walls:
                myGraph[i][j]=1
            elif (i,j) in blanks:
                myGraph[i][j]=0
                
def countSafeArea(myGraph):
    cnt=0
    for i in range(N):
        for j in range(M):
            if myGraph[i][j]==0:
                cnt+=1
    return cnt

for i in range(N):
    for j in range(M):
        if graph[i][j]==2:
            viruses.append((i,j))
        elif graph[i][j]==1:
            walls.append((i,j))
        elif graph[i][j]==0:
            blanks.append((i,j))

possibleWallSets = combinations(blanks,3)

ans=-1

for wallSet in possibleWallSets: # for each possible new wall set
    for wall in wallSet: # for new wall
        graph[wall[0]][wall[1]]=1 # modify graph
        
    for v in viruses: # for each virus,
        myBFS(v[0],v[1]) # perform BFS
        
    curVal = countSafeArea(graph) # count ans
    ans=max(curVal,ans) # update value
    
    restoreGraph(graph) #restore graph
    
print(ans)
