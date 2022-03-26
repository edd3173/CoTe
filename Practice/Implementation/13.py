from itertools import combinations

N,M = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

houses=[]
shops=[]
blanks=[]

for i in range(N):
    for j in range(N):
        if arr[i][j]==0:
            blanks.append((i,j))
        elif arr[i][j]==1:
            houses.append((i,j))
        elif arr[i][j]==2:
            shops.append((i,j))

cityDistance=int(1e9)
shopCombination = combinations(shops,M)

for shopSet in shopCombination:
    currentCityDistance=0
    for customer in houses: # for each customer, find distance
        customerDistance=int(1e9) # current customer's chicken distance
        for shop in shopSet:
            curVal = abs(customer[0]-shop[0])+abs(customer[1]-shop[1])
            customerDistance=min(curVal,customerDistance) # get customer's distance
        currentCityDistance+=customerDistance # add it to currentCityDistance
    cityDistance = min(cityDistance,currentCityDistance) # from ccd, find min to find answer

print(cityDistance)