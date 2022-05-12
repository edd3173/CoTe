N,K = map(int,input().split())
data=[]
for _ in range(N):
    data.append(int(input()))
data.sort()
maxCoin=0
for coin in data:
    if coin <= K:
        maxCoin=coin
#print("maxCoin:",maxCoin)
pCoins=[]
for coin in data:
    if coin <= maxCoin:
        pCoins.append(coin)
#print("Coins:",pCoins)
pCoins.sort(reverse=True)
money = K
ans=0
while money!=0:
    for coin in pCoins:
        ans += money // coin
        money %= coin
        #print("coin:",coin," number:",ans," money:",money)
        
print(ans)