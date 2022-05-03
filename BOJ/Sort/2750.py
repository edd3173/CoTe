import sys

N = int(sys.stdin.readline())
data=[]
counts = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(10001):
    for j in range(counts[i]):
        print(i)