from itertools import combinations
N,M = map(int,input().split())
data = list(map(int,input().split()))

possibleSets = combinations(data,3)
minDist=int(1e9)
ans=0
for pSet in possibleSets:
    if sum(pSet) > M: continue
    curSum = sum(pSet)
    curDist = M-curSum
    if curDist<minDist:
        ans=curSum
        minDist=curDist

print(ans)
        