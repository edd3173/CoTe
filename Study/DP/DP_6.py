"""
    바닥공사
    대단한건없네. 단지 사소한 실수 ㅇㅇ
    
    
    
n=int(input())
dp = [0] * (n+1)

dp[0]=0; dp[1]=1; dp[2]=2; dp[3]=5

for i in range(3,n+1):
  dp[i]=dp[i-1]+dp[i-2]*2 # 세로로 새우는건 안되지1 DP[I-1] 에 포함되잖아!!!!
"""

n=int(input())

dp=[0] * 1001

dp[1]=1
dp[2]=1+1+1

for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796

print(dp[n])
    

 