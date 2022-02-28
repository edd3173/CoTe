"""
snake

idea는 맞지만
코드의 구현이 개쓰레기
보고 배워 제발

"""


n = int(input())
k = int(input())
data = [[0]* (n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a,b = map(int,input().split())
    data[a][b]=1

l=int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c)) # 아예 int로 바꿔서 넣는 것도 ㄱㅊ네.

dx = [0,1,0,-1]; dy = [1,0,-1,0]

def turn(direction,c): #Common Technique for cycle
    if c == "L":
        direction = (direction-1) % 4 
    else:
        direction = (direction+1) % 4 
    return direction

def simulate():
    x,y = 1, 1 # starts in (1,1)
    data[x][y] = 2 # this is snake area
    direction = 0 # Initialy east
    time=0
    idx=0
    q=[(x,y)] # A snake
    
    while True:
        nx=x+dx[direction]
        ny=y+dy[direction]
        
        if 1<=nx and nx <=n and 1<= ny and ny<=n and data[nx][ny] !=2: #Safe area : in map range, no snake
            if data[nx][ny] == 0: # No apple case
                data[nx][ny]=2
                q.append((nx,ny)) # head
                px,py = q.pop(0) # tail
                data[px][py]=0 #remove tail
            if data[nx][ny] == 1:
                data[nx][ny]=2
                q.append((nx,ny)) # 중복되긴하네
        
        else: # Non safe area. escape condition
            time+=1
            return time # 그런데 여기서 return 때려버리는게 아니네? 때려도 되지 않나? ㅇㅇ 상관없음.
        
        x,y = nx,ny # Update
        time += 1
        if idx < l and time == info[idx][0]: # current time == time to spin (info[idx][0] : time val)
            direction = turn(direction,info[idx][1])
            idx+=1 # Next element of info[]
    return time

print(simulate())
            
        
            