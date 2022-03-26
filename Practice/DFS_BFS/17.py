from collections import deque

N,K = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
S,X,Y = map(int,input().split())
viruses=[]
moveSet = [(+1,0),(-1,0),(0,+1),(0,-1)]

for i in range(N):
    for j in range(N):
        if arr[i][j]!=0:
            viruses.append((arr[i][j],i,j,0)) # 0 for time

viruses.sort() # 1찾고 append, 2찾고 append... 할거없이 걍 sort돌린다.

q=deque(viruses)
#print(q)
while q:
    val,px,py,time = q.popleft() # Time을 update하는 tech 기억하기.
    if time==S: break
    for move in moveSet:
        nx=px+move[0]; ny=py+move[1]
        if 0<=nx<N and 0<=ny<N and arr[nx][ny]==0:
            arr[nx][ny]=val
            q.append((val,nx,ny,time+1))

print(arr[X-1][Y-1])