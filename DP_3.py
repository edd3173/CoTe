"""
    효율적인 화폐구성
"""


n,m=list(map(int,input().split()))
arr=[]

for i in range(0,n):
    arr.append(int(input()))

#print(n,m)
#print(arr)

DP=[10001] * (m+1)

# With arrs, pay m

"""
    Here, Idx become m,
    Val become #coin_num
"""
DP[0]=0

min_coin=min(arr)

for coin in arr:
  for j in range(min_coin,m+1): # 만약 j가 min_coin보다 작다면 idx error남.
    if DP[j - coin] != 10001:
      DP[j]=min(DP[j],DP[j-coin]+1)

if DP[m]==10001:
  print(-1)
else:
  print(DP[m])



