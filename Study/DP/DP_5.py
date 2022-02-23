"""
  병사배치하기


  7
  15 11 4 8 5 2 4
"""

n = int(input())
arr = list(map(int,input().split()))
arr.reverse()

dp=[1] * n

#dp[0]==1? right.z

# LIS 알고리즘 : 증가하는 가장 큰 부분순열. 여기서는 4,5,8,11,15가 나오게됨.
for i in range(1,n):
  for j in range(0,i):
    if arr[j]<arr[i]: # 앞이 뒤보다 작음
      dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))


