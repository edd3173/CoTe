
def binarySearch(arr,start,end,target):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return 1
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return 0


N=int(input())
First = list(map(int,input().split()))
First.sort()
fMin=min(First); fMax=max(First)
M=int(input())
Second = list(map(int,input().split()))

for s in Second:
    res=binarySearch(First,0,N-1,s)
    print(res,end=' ')

