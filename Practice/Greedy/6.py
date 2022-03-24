"""
muzzy
문문제 이해도 어렵고 풀이도 어렵다.

다시 풀어봤지만 이건 진짜 아닌거같애...

"""


import heapq
def solution(food_times,k):
    ans=0
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    
    sumTime=0
    prevTime=0 # 이전 단계에서 계산한 시간
    remains=len(food_times)
    
    while sumTime + (q[0][0]-prevTime) * remains <= k:
        now = heapq.heappop(q)[0]
        sumTime += (now-prevTime) * remains
        remains-=1
        prevTime=now
    
    result = q.sort(key= lambda x: x[1])
    
    return result[(k-sumTime)%remains][1]
    
    
    
food_times = [3,1,2]
k=5
result = solution(food_times,k)
print(result)