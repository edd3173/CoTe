

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

    """
    이진탐색 안쓰고 'in'으로도 해결 가능하지만, list쓰면 안됨.
    list는 시간복잡도가 크다!
    따라서 N/M=set(map(int,input().split()))
    한 뒤에 in을 사용한다.
    """