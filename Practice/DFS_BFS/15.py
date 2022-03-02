"""
특정 거리의 도시 찾기
처음에 최단거리 알고리즘인줄 알았다.
최단거리로 해도 될듯?
하지만 거리가 동일하므로 bfs가 더 쉽다!

주의할 점은 visited[]를 만들 필요 없이
dist로 해결 가능. 
그리고 걱정했던 것이 반복하며 이전의 값이 덮어씌워지지 않을까 했는데,
unvisited에만 값을 갱신한다면 그럴 일이 없지.
"""


from collections import deque

n,m,k,x = list(map(int,input().split()))
graph=[[] for _ in range(n+1)]
#print(n,m,k,x)
#visited = [False] * (n+1)
#INF = int(1e9)
distance = [-1] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

def bfs(graph,start,distance):
    q=deque([start])
    distance[start]=0
    
    while q:
        now = q.popleft()
        #print(now,end=' ')
        for i in graph[now]:
            if distance[i] == -1: # unvisited. 
                distance[i]=distance[now]+1
                q.append(i)

bfs(graph,x,distance)

Flag = False

for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        Flag=True

if Flag == False:
    print("-1")
    




