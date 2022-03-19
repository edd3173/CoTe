"""
정확한 순위
"""


n,m = map(int,input().split())
INF=int(1e9)
arr=[[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    src,dst = map(int,input().split())
    arr[src][dst]=1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: arr[i][j]=0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            arr[a][b] = min(arr[a][k]+arr[k][b],arr[a][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j]==INF:
            print("-",end=' ')
        else:
            print(arr[i][j],end=' ')
    print()

ans=0
for point in range(1,n+1):
    #check each (point,point)
    cnt=0
    
    #check horizontally
    for j in range(1,n+1):
        if arr[point][j]!=INF and arr[point][j]!=0:
            cnt+=1
    #check vertically
    for i in range(1,n+1):
        if arr[i][point]!=INF and arr[i][point]!=0:
            cnt+=1
            
    if cnt == n-1:
        ans+=1

print(ans)
            
    