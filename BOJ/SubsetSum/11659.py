import sys
input = sys.stdin.readline
N,M = map(int,input().split())
data= list(map(int,input().split()))

prefix_sum = [0]
sumVal=0
for i in data:
    sumVal+=i
    prefix_sum.append(sumVal)
#print(prefix_sum)

for _ in range(M):
    i,j = map(int,input().split())
    print(prefix_sum[j]-prefix_sum[i-1])