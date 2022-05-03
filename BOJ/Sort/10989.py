counts = [0] * 10001

N=int(input())
for _ in range(N):
    number = int(input())
    counts[number]+=1

for i in range(len(counts)):
    for j in range(counts[i]):
        print(i)
 
