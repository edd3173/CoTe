"""
치킨배달

나쁘지 않지만,
변수의 선언, 계산에 따른 그 변수의 초기화를 주의하자
getDistance()에서 distance는 계속 변하는 값이기 때문에,
선언을 맨 위에하면 값이 이상해진다.
"""

from itertools import combinations



n,m = map(int,input().split())
city=[]
for _ in range(n):
    city.append(list(map(int,input().split())))

chickenPoints=[]
livingPoints=[]

# Find ChickenPoint
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chickenPoints.append([i,j])
        elif city[i][j] == 1:
            livingPoints.append([i,j])

# get distance of current chosen elem of combination
def getDistance(currentPoints):
    # from currentPoints, get chickenDist in arr
    ans=0
    for house in livingPoints: # for each house
        Distance=9999
        h_row=house[0]; h_col=house[1]
        for shop in currentPoints: # for each shop
            s_row=shop[0]; s_col = shop[1]
            Distance=min(Distance,abs(h_row-s_row) + abs(h_col - s_col))
        #print("Current House:",house,"'s Distance:",Distance)
        ans+=Distance
    return ans
    



# use combination to choose 'm' point from chickenPoint
chickenCombination = list(combinations(chickenPoints,m))
ans=9999

# for those points, calc the chicken distance, update answer           
for cPoints in chickenCombination:
     ans = min(ans,getDistance(cPoints))

print(ans)
    