"""
Q-04 : 만들 수 없는 금액

3 2 1 1 9
1 1 2 3 9

"""

n=int(input())
coins = list(map(int,input().split()))
coins.sort()

target=1
for coin in coins:
    if target<coin:
        break
    target+=coin

print(target)