"""
못생긴수
"""

n=int(input())

DP=[-1] * 1001

i2=i3=i5=0
next2,next3,next5=2,3,5
DP[0]=1

for l in range(1,n):
    DP[l] = min(next2,next3,next5)
    if 