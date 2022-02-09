from bisect import bisect_left, bisect_right

"""
Binary Search Ver Recurse
"""

def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid = (start+end) // 2
    if arr[mid]==target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)
    
"""
Binary Search With Iteration
"""

def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end=mid-1
        else:
            start=mid+1
    return None


"""
# Use Bisec to find a number of N in range(a,b)
"""



a=[1,2,4,4,8]
x=4

def countByRange(a,left_val,right_val):
    right=bisect_right(a,right_val)
    left=bisect_left(a,left_val)
    return right-left