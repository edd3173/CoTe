n,m = map(int,input().split())
arr=list(map(int,input().split()))

dp=[]; j=0
for i in range(n):
  dp.append(arr[j:j+m]) # 한번에 입력&assign이 아니라, 입력받고 나서 옮긴다.
  j+=m

#print(dp)

for i in range(n):
  for j in range(1,m):
    if i == 0: # possible direction: from left, leftdown
      # NOTICE: arr[i][j] is wrong! arr is 1d array
      dp[i][j]=dp[i][j]+max(dp[i][j-1],dp[i+1][j-1])
    elif i == n-1: # possible direction: from left, leftup
      dp[i][j]=dp[i][j]+max(dp[i-1][j-1],dp[i][j-1])
    else: # 3 possible direction.
      dp[i][j]=dp[i][j]+max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])

res=0
for i in range(n):
  res=max(res,dp[i][m-1])

print(res)
