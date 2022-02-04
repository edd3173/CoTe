""" 게임 개발 """

n, m = list(map(int, input().split()))

print(n, m)

px, py, pd = list(map(int, input().split()))

# Visited Array
V = [[0] * m for _ in range(n)]
V[px][py] = 1  # Point Visited

# 2D array input
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# N,E,S,W
dx=[-1,0,+1,0]
dy=[0,+1,0,-1]
Dir=pd
cnt=0

# KEYPOINT: To Determine turn time. Look four direction
turn_time=0


def turn_left():
  global Dir
  Dir-=1
  if(Dir==-1):
    Dir=3

while True: #Why? Do this until four direction is all finished -> Fine
  
  turn_left()
  nx=px+dx[Dir]
  ny=py+dy[Dir]

  #2. Check Cond: Not Visited, and Not Sea
  if(V[nx][ny] == 0 and arr[nx][ny]==0):
    # Mark as Visited, Update Position 
    V[nx][ny]=1; px=nx; py=ny
    turn_time=0 # Init.
    cnt+=1 # Update
    continue # Is Necessary? Not Necessary but useful. 이하코드는 실행될 일이 없음.
    # else는 실행 어차피 안되고, turn_time은 0으로 초기화됨. 아래까지 안내려감.
  else:
    #turn_left() WRONG. 이미 위에서 했음.
    turn_time+=1
  
  if(turn_time==4): # 4방향 다 둘러봤는데 없음.
    # Go back.
    nx-=dx[Dir]; ny-=dy[Dir]
    # Is Sea?
    if(arr[nx][ny]==0):
      break # Escape
    else: # Update position
      px=nx; py=ny

print(cnt)

  