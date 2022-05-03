from collections import Counter
import sys
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()

avg = round(sum(data)/N)

med = data[len(data)//2]

occ = -1

myCounter = Counter(data).most_common()
#print(myCounter)

if len(data)>1:
    if myCounter[0][1]==myCounter[1][1]:
        occ = myCounter[1][0]
    else:
        occ = myCounter[0][0]
else:
    occ = myCounter[0][0]

myRange = data[-1] - data[0]

print(avg)
print(med)
print(occ)    
print(myRange)