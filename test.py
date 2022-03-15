from collections import deque

"""
i,j,k = (0,1,2)

A=dist(i,j) = dist(0,1)
B=dist(j,k) = dist(1,2)
C=dist(i,k) = dist(0,2)

1 + 2 != 1 : fail -> A+B = C 를 만족시켜야
bfs(i)를 돌리면
A=dist(i,j) = dist[j]
C=dist(i,k) = dist[k]
B=dist(j,k) = ?
However, we should satisfy: A+B = C
B must equal to C-A

따라서, i를 0부터 n 까지 bfs를 돌려. bfs(i)
그리고, 이중 for문으로 dist[j]와 dist[k]를 잡아. ->여기까지 3중
여기서 또 bfs를 돌려? bfs(j)를 돌려서 dist'[k]를 구해.
# dist[j] + dist'[k] == dist[k]인지 확인해. 맞으면 저장.
이지랄을 해야한다고?

"""


def restoreDistance(distance):
    for ele in distance:
          ele=-1

def bfs(graph,start,distance):
    restoreDistance(distance)
    
    #print("BFS HELLO!!!",distance)
    
    q=deque([start])
    distance[start]=0
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == -1: # unvisited. 
                distance[i]=distance[now]+1
                q.append(i)

def solution(n, edges):
    answer = 0
    for edge in edges: # for each edge
      x,y = edge
      graph[x].append(y)
      graph[y].append(x) # since this is no-direction graph
    
    for i in range(0,n):
        bfs(graph,i,distance)
        for j in range(0,n) :
            for k in range(0,n) :
                print("(i,j,k) : ",i,j,k)
                print("bfs in i:",i)
               
                print("distance of bfs(i): ",distance)
                
                DIST_IJ = distance[j]
                DIST_IK = distance[k]
                print("dist(i,j), dist(i,k) : ",DIST_IJ, DIST_IK)
                
                # for bfs(j), restore distance
                bfs(graph,j,distance)
                print("distance of bfs(j): ",distance)
                DIST_JK = distance[k]
                
                
                print("dist(i,j),dist(j,k),dist(i,k):",DIST_IJ,DIST_JK,DIST_IK)
                
                """
                if DIST_IJ + DIST_JK == DIST_IK and DIST_IJ!=0 and DIST_IK!=0 and DIST_JK!=0:
                    if i!=j and j!=k and i!=k:
                        print("(i,j,k) : ",i,j,k)
                        print("dist(i,j),dist(j,k),dist(i,k):",DIST_IJ,DIST_JK,DIST_IK)
                        answer+=1
                """
    return answer
      

n=5
edges=[[0,1],[0,2],[1,3],[1,4]]
graph = [[] for _ in range(n)]
distance=[-1] * n
result = solution(n,edges)

"""
for edge in edges: # for each edge
    x,y = edge
    graph[x].append(y)
    graph[y].append(x) # since this is no-direction graph

bfs(graph,0,distance)
print(distance)
"""
#print(result)


# distance(i, j) + distance(j, k) = distance(i, k)