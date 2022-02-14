""" 숫자 카드 게임 """

#2d array examples...
"""
arr=[[0] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    arr[i][j]=1

for i in arr:
  for j in i:
    print(j,end=' ')
  print()
"""

n,m = map(int,input().split())
max_val = 0

for _ in range(0,n):
  row = list(map(int,input().split()))
  max_val=max(max_val,min(row))


print(max_val)
