"""
감시 피하기


구현의 어려움.
머리를 더 쓰고, 손을 덜 쓰자.
로직을 꼼꼼하게 생각하기.
"""

from itertools import combinations


n = int(input())
arr =[]
for _ in range(n):
    arr.append(list(input().split()))

#print(arr)

obstacleNum = 3

Teachers=[]
Students=[]
Blanks=[]

for i in range(n):
    for j in range(n):
        if arr[i][j]=='X':
            Blanks.append((i,j))
        elif arr[i][j]=='S':
            Students.append((i,j))
        elif arr[i][j]=='T':
            Teachers.append((i,j))


"""
요것도 괜찮지만, 더 좋은 방법이 있다.

"""
def restoreArray():
    for (i,j) in Blanks:
        arr[i][j]='X'
    for (i,j) in Students:
        arr[i][j]='S'
    for (i,j) in Teachers:
        arr[i][j]='T'


"""
맥락은 맞지만, 
논리가 부족했다.
벽을 만난다면, 그 다음에 학생을 만나는 경우는 생각 x.
즉 학생을 만났을 때 그 이전에 벽이 있었는지 생각 안해도 된다.
왜? 학생을 만나면 즉시 true 리턴한다.
벽을 만나면 즉시 false 리턴한다. 그 다음은 내 알바 아님.
만약 그 이전에 학생을 만났다면, 이미 true 리턴했을 것.
따라서 학생 다음의 학생, 벽 다음의 학생, 이런 것은 부의미.

"""

def Watch(px,py,dir):
    if dir == 0: # N
        while px >= 0:
            if arr[px][py]=='O':
                return False
            elif arr[px][py]=='S':
                return True
            px-=1
            
    elif dir == 1: # S
        while px < n:
            if arr[px][py]=='O':
                return False
            elif arr[px][py]=='S':
                return True
            px+=1
            
    elif dir == 2: # E
        while py < n:
            if arr[px][py]=='O':
                return False
            elif arr[px][py]=='S':
                return True
            py+=1
            
    elif dir == 3: # W
        while py >= 0:
            if arr[px][py]=='O':
                return False
            elif arr[px][py]=='S':
                return True
            py-=1
            
    return False

def process():
    for x,y in Teachers:
        for i in range(4):
            if Watch(x,y,i): # 하나라도 보이면, 즉시 종료.
                return True
    return False # 고난의 행군 끝에 정답.
    


ObstaclesList = combinations(Blanks,obstacleNum)
#print(Obstacles)

Flag = False

for Obstacles in ObstaclesList:
    
    # set obstacle
    for Obstacle in Obstacles:    
        o_x=Obstacle[0]
        o_y=Obstacle[1]
        arr[o_x][o_y]='O'
        
    #for teacher in Teachers: # for teachers
    
    """
    우리가 원하는 상황을 찾는 즉시 탈출.
    """
    if process() == False:
        Flag=True
        break
    
    
    """
    이런 식으로 되돌릴 수 있다.
    
    """
    for Obstacle in Obstacles:    
        o_x=Obstacle[0]
        o_y=Obstacle[1]
        arr[o_x][o_y]='X'

if Flag:
    print("YES")
else:
    print("NO")
     
    