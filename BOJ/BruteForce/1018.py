
N,M = map(int,input().split())
data=[]
for _ in range(N):
    data.append(list(input()))

whiteBoard = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W']
]

blackBoard=[
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B']
]

def cmpWhite(target):
    cnt=0
    for i in range(8):
        for j in range(8):
            if target[i][j]!=whiteBoard[i][j]:
                cnt+=1
    return cnt   

def cmpBlack(target):
    cnt=0
    for i in range(8):
        for j in range(8):
            if target[i][j]!=blackBoard[i][j]:
                cnt+=1
    return cnt

ans=int(1e9)
for i in range(N-7):
    for j in range(M-7):
        tempArr = [[-1] * 8 for _ in range(8)]
        for k in range(8):
            for l in range(8):
                tempArr[k][l]=data[i+k][j+l]
        curVal = min(cmpWhite(tempArr),cmpBlack(tempArr))
        ans = min(ans,curVal)

print(ans)
        
        

