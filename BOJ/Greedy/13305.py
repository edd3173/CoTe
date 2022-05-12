N=int(input())
roadLen = list(map(int,input().split()))
prices = list(map(int,input().split()))

totalLen = sum(roadLen)
totalPrice = 0

curLen=0
curPos=0
curPrice=prices[curPos]
"""
다음 가장 가까운, 현재보다 작은 곳을 찾는다. 그 전까지 주유함.


    2      3      1      4
5 ---- 2 ----- 1 ---- 4 ---- 3

5*2 + 2*3 +  1*(1+4)

"""

minPrice = min(prices)

while curPos != N-1: # start with pos 0
    # find next pos
    nextPos = -1
    
    if curPrice == minPrice:
        nextPos = N-1
    else:
        for i in range(curPos+1, totalLen):
            if prices[i] < curPrice:
                nextPos=i
                break
    
    # calc roadLen to nextPos
    # index 1 to 3 -> road 1 to 2
    nextRoadLen=0
    for i in range(curPos, nextPos):
        nextRoadLen += roadLen[i]
    
    # calc price to nextPos
    totalPrice += nextRoadLen * curPrice
    
    # update values
    curPos = nextPos
    curPrice = prices[curPos]

print(totalPrice)