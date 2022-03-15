from bisect import bisect_right, bisect_left

N,x = map(int,input().split())
arr = list(map(int,input().split()))

left_idx = bisect_left(arr,x)
right_idx = bisect_right(arr,x)

#print(left_idx,right_idx)

if left_idx == len(arr) or right_idx == len(arr):
    print(-1)
else:
    ans = right_idx-left_idx
    print(ans)
    