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

Max=-int(1e9)

for _ in range(n):
  cur = list(map(int,input().split()))
  curVal = min(cur)
  if Max < curVal:
    Max = curVal

print(Max)
