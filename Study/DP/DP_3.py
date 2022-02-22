n,m = map(int,input().split())
coins=[]

# Initializing for 10001 b/c smallest coin val is 1.
dp=[10001] * m 
for _ in range(n):
  coins.append(int(input()))


dp[0]=0 # important! For calculation. dp[2]=dp[0]+1 같이 계산이 된다. 필수 시작조건.
min_coin = min(coins)
for coin in coins:
  for j in range(min_coin,m+1): # if j in range(<min_coin,m+1) then index oor err
    if dp[j-coin]!= 10001: # if we can go further step : j-coin to j;
      dp[j]=min(dp[j],dp[j-coin]+1) 