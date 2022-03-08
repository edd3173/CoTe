from collections import deque

n,l,r = map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))


move_set = [(+1,0),(-1,0),(0,+1),(0,-1)]


def isAvailable(px,py,nx,ny):
    val = abs(arr[px][py]-arr[nx][ny])
    if val <=r and val >= l:
        return True
    else:
        return False

def bfs(px,py, idx): # idx가 추가됬네. 이게 뭐임. bfs를 돌리는 횟수. (unvisited인 곳을 찾는경우)
    q=deque()
    q.append((px,py))
    Unite = []
    Unite.append((px,py))
    union[px][py]=idx
    unionSum = arr[px][py] # Sum of current union
    count = 1 # count of current Unite. need?
    
    while q:
        #now = q.popleft()
        #px=now[0]; py=now[1]
        
        px,py = q.popleft()  # This style is better
      
        # for each move
        for move in move_set:
            #print("current Move:", move)
            nx=px+move[0]
            ny=py+move[1]
            
            #print("px,py,nx,ny: ",px,py,nx,ny)
            
            #if nx< 0 or nx>=n or ny<0 or ny>=n or isAvailable(px,py,nx,ny)==False:
                #if nx == 1 and ny == 1:
                 #   print("arr[nx][ny]:",arr[nx][ny])
                  #  print("arr[px][ppy:", arr[px][py])
                #continue
            if 0<= nx <n and 0<= ny < n and union[nx][ny]==-1: # find 'true' condition
                if isAvailable(px,py,nx,ny):
                    #print("Avaliable Point: (px,py,nx,ny) :", px,py,nx,ny)
                    q.append((nx,ny))
                    union[nx][ny]=idx
                    unionSum += arr[nx][ny]
                    count+=1
                    union.append((nx,ny))
                    
                    
                    #if(UniteSum==0): Dont' need. we initialize at start
                     #   UniteSum = arr[px][py]
                      #  Unite.append((px,py))
                    #UniteSum += arr[nx][ny]
                    # do some math
                    
    #print("UniteSum : ",UniteSum)
    #print("Unites : ", Unite)
    
    # After queue        
    for x,y in Unite:
        arr[x][y] = unionSum // count # // is NOT remnant. remnant is %
    


#print("-----------------------------")

totalCount=0

while True: # repeat bfs until condition is set
    union = [[-1]* n for _ in range(n)] # Visited 대신에 group identitiy가 존재하는 배열을 썼구나.
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # not processed
                bfs(i,j,idx) # process
                idx+=1
                
    if idx == n*n: # checked all array in union[][]
        break
    totalCount += 1 # update when bfs is done
            
print(totalCount)
   
   
         
"""            
from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색 (BFS)을 위한 큐 라이브러리 사용
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가하기
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)
"""    
    