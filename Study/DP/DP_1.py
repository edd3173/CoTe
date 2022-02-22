"""
개미전사
"""

N=int(input())
Arr=list(map(int,input().split()))
DP=[0]*100


"""

1
5

2
5 1

3

5 1 2

4
5 1 2 3

5
5 1 2 3 6


6
5 1 2 3 6 11

M[0] = 
Arr[0]

M[1] = 
if Arr[1] > Arr[0]:
  M[1]=Arr[1]
else:
  M[1]=Arr[0]

M[2] =  
max(Arr[1], Arr[0]+Arr[2]) 

M[3] = 
max(Arr[0]+Arr[2], Arr[1]+Arr[3])

M[4] = 
max(Arr[0]+Arr[2]+Arr[4], Arr[1]+Arr[3])

M[5] = 
max(Arr[0]+Arr[2]+Arr[4],Arr[1]+Arr[3]+Arr[5])


M[i]=
max( 
  M[i-1],
  M[i-2]+Arr[i]
)

큰 그림을 볼 수 있도록 노력하자.
저게 망하는 이 가, dp[0]과 dp[1]이 정해지지 않은 상황에서
저렇게 식쓰려니까 망함. 


"""

DP[0]=Arr[0]
DP[1]=max(Arr[0],Arr[1])

for i in range(2,N):
  DP[i]=max(DP[i-1],DP[i-2]+Arr[i])

print(DP[N-1])