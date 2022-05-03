
"""
패배한 기분이다...
"""

N = int(input())
data=[]
for _ in range(N):
    x,y = map(int,input().split())
    data.append((x,y))


for a in data:
    currentRank=1
    for b in data:
        if a[0]<b[0] and a[1]<b[1]:
            currentRank+=1
    print(currentRank)

