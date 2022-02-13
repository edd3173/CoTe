""" 숫자 카드 게임 """


n,m = map(int,input().split())

res=0

#2d array examples...
"""
arr=[[0 for col in range(m)] for row in range(n)]

for i in range(n):
  for j in range(m):
    arr[i][j]=1

for i in arr:
  for j in i:
    print(j,end=' ')
  print()
"""

for i in range(n):
  curRow=list(map(int,input().split()))
  curMin=min(curRow)
  if curMin > res:
    res=curMin

print(res)

