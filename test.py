"""
https://www.acmicpc.net/problem/18428

찾을 수 있는 경우와 없는 경우.
모두를 확인할 수 있게
Flag를 global이 아니라 obset 안의 regional로 set 해야한다!

"""




from itertools import combinations

N=int(input())
Graph=[]
Blanks=[]; Teachers=[]; Students=[]; Obstacles=[]
MoveSet = [(+1,0),(-1,0),(0,+1),(0,-1)]
#get graph
for _ in range(N):
    Graph.append(list(input().split()))

#print(Graph)

# get info
for i in range(N):
    for j in range(N):
        if Graph[i][j]=='X':
            Blanks.append((i,j))
        elif Graph[i][j]=='S':
            Students.append((i,j))
        elif Graph[i][j]=='T':
            Teachers.append((i,j))



def checkDir(dir,tx,ty):
    while True:
        
        tx+=dir[0]; ty+=dir[1]
        
        if tx<0 or tx>=N or ty<0 or ty>=N:
            break
        
        if Graph[tx][ty]=='O':
            return False
        elif Graph[tx][ty]=='S':
            return True

def findStudent(Teacher):
    tx=Teacher[0]; ty=Teacher[1]
    for dir in MoveSet: # for each direction
        res = checkDir(dir,tx,ty) # check if student exists
        if res==True: #found student
            return True  # return true
    return False # return false


PossibleObstacleSet = combinations(Blanks,3)

#Flag=False # global flag. Teacher not found student.
for obstacleSet in PossibleObstacleSet: # for possible obstacle scenario
    Flag=False # global flag. Teacher not found student.

    for obstacle in obstacleSet: # for each obstacle
        Graph[obstacle[0]][obstacle[1]] = 'O' # modify graph
    
    for teacher in Teachers: # for each teacher
        if findStudent(teacher): # find student
            Flag=True # if student found
            break # break. answer is NO. 감시를 피할수 없음.
    
    if not Flag: # answer is YES
        break # this is the place to break.
    
    for obstacle in obstacleSet: # for each obstacle
        Graph[obstacle[0]][obstacle[1]] = 'X' # restore graph
    

if not Flag: # student all hidden
    print("YES") # match the request
else: # able to found student
    print("NO") # Not able to hide. answer NO