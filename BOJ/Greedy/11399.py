from sys import prefix


N=int(input())
data= list(map(int,input().split()))
#print(data)
data.sort()
#print(data)

prefixSum=[0]

sumVal=0
for d in data:
    sumVal+=d
    prefixSum.append(sumVal)

ans=0
for i in range(N+1):
    ans += (prefixSum[i])

print(ans)