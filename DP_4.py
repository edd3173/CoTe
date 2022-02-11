"""
  금광문제

  아! 스포당해버렸다!
"""

n,m = list(map(int,input().split()))
arr=list(map(int,input().split()))

dp=[]
idx=0

for i in range(n):
  dp.append(arr[idx:idx+m])
  idx+=m


for j in range(1,m):
  for i in range(n): # Double for loop? Simply?
    if i+1==n: # This must from left up or left
      dp[i][j]=dp[i][j]+max(dp[i-1][j-1],dp[i][j-1]) # 바닥을 뚫음.
    elif i==0: # This must from left down or left
      dp[i][j]=dp[i][j]+max(dp[i][j-1],dp[i+1][j-1])
    else: # From left or leftdown or leftup
      dp[i][j]=dp[i][j]+max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])

res=0
for i in range(n):
  for j in range(m):
    res=max(res,dp[i][j])

print(res)


