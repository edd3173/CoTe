""" Ice Cream """

n,m = list(map(int,input().split()))

graph=[]
for i in range(n):
  graph.append(list(map(int,input()))) # no split. 1 0 1 1 이 아니라, 1011로 입력받으니까

visited = [[False]* m for _ in range(n)]
cnt=0

def DFS(x,y): # Return type 정의 없이 
  if x<0 or y<0 or x>=n or y>=m:
    return False # Return 가능
  if graph[x][y] == 0: # At start, return False
    #Now we search. How?
    graph[x][y]=1
    DFS(x+1,y)
    DFS(x-1,y)
    DFS(x,y+1)
    DFS(x,y-1)
    # 처음 dfs에 대해서만 True를 리턴하게 한다.
    return True # At last, return True. WHEN all zeros are gone, and switched to one. (iterated all chunk)
  return False

for i in range(n):
  for j in range(m):
    if DFS(i,j)==True:
      cnt+=1

print(cnt)


