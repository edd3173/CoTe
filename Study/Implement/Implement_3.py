
n,m = map(int,input().split())
px,py,_dir = map(int,input().split())

arr=[]
for _ in range(n):
  arr.append(list(map(int,input().split())))

visited=[[False]* m for _ in range(n)]

# North,East,South,West
dx=[-1,0,+1,0]
dy=[0,+1,0,-1]

def change_direction():
  global _dir
  _dir -= 1
  if(_dir==-1): _dir=3
  """
  Turn_Time은 main으로 가야된대.

  global dirCnt
  dirCnt+=1
  """

# Initialize
turn_time=0
visited[px][py]=True # Mark Visited! Important!
res=1 # So initial visit_num equal 1

while True:
   
  # Step1. Rotate. _dir=0, 
  change_direction()
  
  # _dir == 3, means dx/dy[_dir] goes West
  nx=px+dx[_dir]
  ny=py+dy[_dir]

  # Not Visited, Valid
  if(arr[nx][ny]==0 and visited[nx][ny]==False):
    visited[nx][ny]=True # Mark
    px=nx; py=ny; # Update Pos
    turn_time=0 # Initialize turns
    res+=1
    continue # Finish. Is Necessary? Not Necessary but useful. 이하코드는 실행될 일이 없음.
    # else는 실행 어차피 안되고, turn_time은 0으로 초기화됨. 아래까지 안내려감.
  else: # go back to step 1. no need to change_dir, since it is done in step 1
    turn_time+=1

  # Step3. Check for escapes
  if turn_time==4:
    nx=px-dx[_dir] # px: original. px-dx : 1step go back.
    ny=py-dy[_dir] # py : same

    if arr[nx][ny]==1: # Escape condition
      break
    else: 
      px=nx; py=ny; # Update Pos
    turn_time=0 # Initialize turns

print(res)



  




  
