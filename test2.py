
import heapq

food_times = [3,1,2]
q=[]

for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i],i+1))

now = heapq.heappop(q)[0]
print(now)
print(q)