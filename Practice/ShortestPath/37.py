import heapq

n=int(input())
m=int(input())
INF = int(1e9)

arr=[[INF]* (n+1) for _ in range(n+1)]

for _ in range(m):
    x,y,c = map(int,input().split())
    arr[x][y]=min(arr[x][y],c)

def FW():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                arr[i][j] = min(arr[i][k]+arr[k][j],arr[i][j])


for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: 
            arr[i][j]=0
        
FW()

for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j]==INF:
            print("0", end=' ')
        else:
            print(arr[i][j],end=' ')
    print()