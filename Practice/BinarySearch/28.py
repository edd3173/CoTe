from bisect import bisect_left

"""
코드 변형!

"""



def binary_search(arr,start,end):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            start = mid+1
        else:
            end = mid-1
    return None


n=int(input())
arr=list(map(int,input().split()))

idx = binary_search(arr,0,n-1)
if idx==None:
    print(-1)
else:
    print(idx)
