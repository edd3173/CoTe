

"""
    부품찾기
"""

n=int(input())
N=list(map(int,input().split()))
m=int(input())
M=list(map(int,input().split()))

def binary_search(arr,target,start,end):
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid] < target):
            start=mid+1
        else:
            end=mid-1
    return None

for i in M:
    res=binary_search(N,i,0,len(N)-1)
    if(res==None):
        print("No",end=' ')
    else:
        print("Yes",end=' ')

    