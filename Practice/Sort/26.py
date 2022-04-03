import heapq

"Time Complexity : Use heap"

n=int(input())
h=[]
for _ in range(n):
    heapq.heappush(h,int(input()))

ans=0

while len(h)!=1: # until single value left
    first = heapq.heappop(h) # pop minimum
    second = heapq.heappop(h) # pop second minimum
    ans += first+second # add to value
    heapq.heappush(h,first+second) # push merged card

print(ans)