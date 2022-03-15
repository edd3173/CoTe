






"""
(0,0)
(8-1,0) -> (7,0)
(8-1,0+8-2) -> (7,6)
(8-1 - 4(7-3),0+8-2) -> (3,6)
(3,6 - (6-2)) -> (3,4)
(4,4)


1. to x, + (n-1)
2. to y, + (n-2)
3. if n%2 == 0:
n//2 , n//2
else:
to x, n-1-posX-3

4. to (n-1 // 2, n-1//2)       

"""

def printArr():
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()


n=9
arr = [[0] * (n) for _ in range(n)]

n-=1 # To fit array

# curve North:
curVal=1
curX=0
curY=0

#first sentence
for i in range(n):
    arr[i][curY]=curVal
    curVal+=1
    curX=i

#printArr()

#second sentence
for j in range(n-2):
    arr[curX][j]=curVal
    curVal+=1
    curY=j

#printArr()

#third sentence
for k in range(0,n-3):
    arr[curX][curY]=curVal
    curVal+=1
    curX=curX-1

printArr()

# fourth sentence
for l in range(1,n-1-4):
    arr[curX][curY-l]=curVal
    curVal+=1
    curY=curY-1

#last sentence
arr[curX-1][curY]=curVal




