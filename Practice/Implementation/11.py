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
    info.append((int(x),c)) # 아예 int로 바꿔서 넣는 것도 ㄱㅊ네. -> Checked

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



"""
<MYCODE>

N=int(input())
K=int(input())
appleInfo=[]
rotateInfo=[]
for _ in range(K):
    r,c = map(int,input().split())
    appleInfo.append((r,c))
L=int(input())
for _ in range(L):
    X,C = input().split()
    rotateInfo.append((int(X),C))

# D : moveSet[i++], C : moveSet[i--]
moveSet = [(0,+1),(+1,0),(0,-1),(-1,0)]
snake=[]
px=1; py=1
snake.append((px,py)) # init snake
dirIdx=0 # initial direction
curHead = snake[0] # initial head
Time=0

def updateDir(Time,dirIdx):
    for info in rotateInfo: # iterate rotateInfo
        if Time==info[0]: # if that time
            if info[1]=='D': # rotate right 
                dirIdx+=1
                if dirIdx == 4: dirIdx=0 # OOR
            else:
                dirIdx-=1 # rotate left
                if dirIdx == -1: dirIdx=3 # OOR
    return dirIdx
    
        

while True: # until snake bumps wall, or its body
    Time+=1 # updates time
    # print("Time:",Time)
    # print("Snake before:", snake)
    # print("Direction: ",moveSet[dirIdx])
    
    curHead = snake[-1] 
    nextHead = (curHead[0]+moveSet[dirIdx][0],curHead[1]+moveSet[dirIdx][1]) # find next head
    # print("nextHead : ",nextHead)
    
    # ESCAPE : # newHead is OOR, or bump it's body
    if nextHead[0] > N or nextHead[1] > N or nextHead[0] <=0 or nextHead[1] <=0 \
        or nextHead in snake: 
        # print("Escape in Time,",Time)
        # print("newHead ",nextHead,"is OOR")
        # print("or nextHead :",nextHead,"bump its body snake:",snake)
        break
    
    if nextHead in appleInfo: # exists apple
        appleInfo.remove(nextHead) # remove apple
        # tail doesn't move
        snake.append(nextHead) # append the head
    else:
        snake.pop(0) # remove the tail
        snake.append(nextHead) # append the head

    # print("snake after: ",snake)
    # print("Updating dir:")
    dirIdx=updateDir(Time,dirIdx) # CAUTION! direction update AFTER move
    #print("newDirection : ",moveSet[dirIdx])
    
print(Time)
"""
            
        
            