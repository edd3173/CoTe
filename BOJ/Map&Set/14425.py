N,M = map(int,input().split())
S = []
T = []
for _ in range(N):
    S.append(input().strip())
    
    
for _ in range(M):
    T.append(input().strip())

S = set(S)
ans=0
for t in T:
    if t in S: ans+=1

print(ans)