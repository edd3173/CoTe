import sys
N=int(sys.stdin.readline().rstrip())
data=[]
for _ in range(N):
    x,y = sys.stdin.readline().rstrip().split()
    x=int(x)
    data.append((x,y))

data.sort(key=lambda x: x[0])

for d in data:
    print(d[0],d[1])