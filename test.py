def binary_search(arr,target,start,end):
    while start<=end:
        mid = (start+end) // 2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return None

N,M = map(int,input().split())
arr = list(map(int,input()))