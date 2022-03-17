n=int(input())
T=[]; P=[]
for _ in range(n):
    t,p = map(int,input().split())
    T.append(t) ; P.append(p)
    
DP=[0] * n

"""
optimal substructure:

// let DP[i] : max pay til dayh i

어렵다.

"""
maxVal=0

for i in range(n-1,-1,-1):
    time = t[i]+i
    if time<=n:
        DP[i] = max(p[i]+DP[time],maxVal)
        maxVal=p[i]
    else:
        DP[i]=maxVal