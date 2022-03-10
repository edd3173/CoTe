n,m = map(int,input().split())
coins=[]

# Initializing for 10001 b/c smallest coin val is 1.
dp=[10001] * m 
for _ in range(n):
  coins.append(int(input()))


dp[0]=0 # important! For calculation. dp[2]=dp[0]+1 같이 계산이 된다. 필수 시작조건.

for i in range(n): # for coin iteration
  for j in range(coins[i],m+1): # coins[i],since we must calc for each coin.
    if dp[j-coins[i]]!=10001:
      dp[j]=min(dp[j-coins[i]]+1,dp[j])