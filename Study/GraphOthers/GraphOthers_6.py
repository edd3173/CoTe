"""
커리큘럼

진짜 어렵다!

"""

from collections import deque
import copy


n=int(input())
indegree=[0] * (n+1)
graph=[[] for i in range(n+1)]
times=[0] * (n+1)

for i in range(n):
    data = list(map(int,input().split()))
    times[i]=data[0] # for later use
    precourses=data[1:-1]
    for course in precourses:
        indegree[i]+=1
        
        # IMPORTANT! graph에서 x(선수)->i(후수)이므로
        # 방향그래프상, graph[x]에 i가 append되는게 맞지.
        # Topological sort에 대한 이해 부족.
        graph[course].append(i) 

def topological_sort():
    result = copy.deepcopy(times)
    q=deque()
    
    for i in range(1,n+1):
        if indegree[i]==1:
            q.append(i)
            
    while q:
        now=q.popleft()
        result.append(now)
        for i in graph[now]:
            result[i]=max(result[i],result[now]+times[i])
            indegree[i]-=1
            if(indegree[i]==0):
                q.append(i)
                
    for i in range(1,n+1):
        print(result[i])
        
        
topological_sort()

