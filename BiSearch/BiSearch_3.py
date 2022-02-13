"""
정렬된 배열에서 특정 수의 갯수 구하기
"""


from bisect import bisect_left, bisect_right

n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))

# Use Bisec to find a number of N in range(a,b)

left=bisect_left(arr,m)
right=bisect_right(arr,m)

print(right-left)

