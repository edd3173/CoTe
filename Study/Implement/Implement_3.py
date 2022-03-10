n,m = map(int,input().split())
px,py,d = map(int,input().split())
arr=[]
for _ in range(n):
  arr.append(list(map(int,input().split())))

visited = [[False]*m for _ in range(n)]
visited[px][py]=True

directions = [0,1,2,3]
move_set = [(-1,0),(0,+1),(+1,0),(0,-1)]

def turn_left():
  global d
  d -= 1
  if d == -1:
    d += 4

  # others"?

tVal=0
cnt=1

while True:

  turn_left()
  
  nx=px+move_set[d][0]
  ny=py+move_set[d][1]

  # OOR, or Visited, or Sea
  if nx<0 or nx>=n or ny<0 or ny>=m or arr[nx][ny] == 1 or visited[nx][ny]==True:
    tVal +=1 # IMPORTANT
    

  # if okay, visit and update position
  else:
    visited[nx][ny]=True
    px=nx; py=ny
    cnt+=1; tVal=0
    continue # 컨티뉴가 이쪽에 붙어야지 ㅇㅇ

  # turned 4 times.
  if(tVal == 4):
    px -= move_set[d][0]
    py -= move_set[d][1]
    if arr[px][py]==0:
      break
    else:
      nx=px; ny=py
    tVal=0 # 이것도 잊지 말고

print(cnt)


    
  


  
  
  