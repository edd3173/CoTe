"""
1로만들기
"""

#Initial value

# 1,/2,/3,/5로 값을 갱신해야 최소값이 되지 않을까? ㅇㅇ 맞음.


# f(n)=g(n/5)+ a
# 가 아니라, f(5n)=f(n)+a 인가 -> 상관없음



# 큰 range안에 4번을 하면 되잖아! 값이 계속 갱신되게!
#그리고 range는 (2,n+1) 고정이지. 왜냐면 2,3 등에서 DP[1~5]의 값이 바뀔수 있으니까!
# 물론 여기서 min을 연쇄적으로 해야함.

"""

# x-=1
for i in range(1,n+1):
  DP[i]=DP[i-1]+1

# x/=2
for i in range(2,n+1):
  if i%2 == 0:
    DP[i]=DP[i//2]+1

# x/=3
for i in range(3,n+1):
  if i%3 == 0:
    DP[i]=DP[i//3]+1

# x/=5
for i in range(5,n+1):
  if i%5 == 0:
    DP[i]=DP[i//5]+1

print(DP[n])
"""


n=int(input())
INF=int(1e9)
dp=[INF]* 30001

dp[1]=0;dp[2]=1;dp[3]=1;dp[4]=2;dp[5]=1



for i in range(6,n+1): # 4개 조건이 '한번에' 믂여야
  dp[i]=dp[i-1]+1
  
  if i%2 == 0:
    dp[i]=min(dp[i],dp[i//2]+1)
    
  if i%3 == 0:
    dp[i]=min(dp[i],dp[i//3]+1)
    
  if i%5 == 0:
    dp[i]=min(dp[i],dp[i//5]+1)

print(dp[n])
