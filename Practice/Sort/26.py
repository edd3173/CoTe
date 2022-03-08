
import heapq

n=int(input())
cards=[]
for _ in range(n):
    heapq.heappush(cards,int(input()))
    #arr.append(int(input()))
#arr.sort()
Sum=0
#print(arr)

'''
10
20
40
50

10+20 = 30
+
30+40 = 70
+
70+50 = 120


계속 연쇄적으로 더해지는 꼴이 트리랑 비슷하네!!!!

'''

if n==1:
    Sum=0
else:
    while True:
        
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        now = first+second
        Sum+=now
        if len(cards)==0:
            break
        heapq.heappush(cards,now)
    
print(Sum)

#print(ans)