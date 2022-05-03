import sys
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    data.append((x,y))

data.sort(key=lambda x : (x[0], x[1]))

for d in data:
    print(d[0],d[1]) 