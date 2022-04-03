import heapq

n=int(input())
h=[]
for _ in range(n):
    heapq.heappush(h,int(input()))

ans=0

while len(h)!=1:
    first = heapq.heappop(h)
    second = heapq.heappop(h)
    ans += first+second
    heapq.heappush(h,first+second)

print(ans)