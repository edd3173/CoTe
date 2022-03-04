"""
경쟁적 전염
"""
from collections import deque
from operator import truediv
n,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
ts,tx,ty = map(int,input().split())
move_set = [(+1,0),(-1,0),(0,+1),(0,-1)]
data=[]

for i in range(n):
    for j in range(n):
       if arr[i][j] != 0 :
           # insert type,time?,px,py
           data.append((arr[i][j],0,i,j))

"""
Queue를 어떻게 구성하는가! 잘 봐라
"""


data.sort() # sort by type. since small type goes first
q=deque(data)

while q:
    type,time,x,y = q.popleft()
    if time == ts:
        break
    
    for move in move_set:
        nx = x+move[0]
        ny = y+move[1]
        
        
        # WHAT DIFFERENCE?
        
        
        if nx<0 or nx>=n or ny<0 or ny>=n or arr[nx][ny]!=0:
            continue
    
        arr[nx][ny]=type
        q.append((type,time+1,nx,ny))
        
        
        """
        if 0<=nx and nx<n and 0<=ny and ny<n:
            if arr[nx][ny]==0:
                arr[nx][ny]=type
                q.append((type,time+1,nx,ny))
        """


print(arr[tx-1][ty-1])

"""
KeyPoint : Queue를 3개를 만드는 것이 아니라, 큐에 작은 순서대로 넣는 것!
"""
        

