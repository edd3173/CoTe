n,m = map(int,input().split())
tempArr = list(map(int,input().split()))
realArr = []
for i in range(0,n):
    cur = tempArr[i*m:i*m+m]
    realArr.append(cur)

#print(realArr)

dp = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        dp[i][j]=realArr[i][j]

print(dp)



"""
FOR loop에서 IJ의 순서에 따라 답이 틀림!
최종적으로 가로 방향으로 진행을 하니까!!!
그러네;;;
"""

for j in range(1,m): 
    for i in range(n): 
        if i==0: # top
            dp[i][j] = max(dp[i][j-1],dp[i+1][j-1])+realArr[i][j]
        elif i==n-1: # bottom
            dp[i][j] = max(dp[i-1][j-1],dp[i][j-1])+realArr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])+realArr[i][j]

print(dp)

ans=-1
for i in range(n):
    ans=max(ans,dp[i][m-1])

print(ans)