
"""
Selection Sort
"""


arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[j]<=arr[min_idx]: #find index
            min_idx=j
        #swap values of idx
    #tmp=arr[i]; arr[i]=arr[min_idx]; arr[min_idx]=arr[i]
    # Or Swap like this: Worth Study
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)


"""
Insertion Sort
"""

arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(arr)): # 5,9,0,3 ...
    for j in range(i,0,-1): # 5에서 역방향으로 -1씩 이동
        if arr[j]<=arr[j-1]: # 현재 idx(현재)와 idx-1(왼쪽)의 val을 비교. 어 idx가 더 작네?
            arr[j], arr[j-1] = arr[j-1], arr[j] # 그럼 왼쪽으로 가야지
        else: # 어 이제 왼쪽거보다 지금이 더 큰데?
            break # 그럼 이동할 필요없지
print(arr)


"""
Quick Sort
"""

# Quick Sort

def quick_sort(arr,start,end):
  if start>=end:
    return
  pivot = start
  left = start+1
  right = end
  while left<= right: # 엇갈릴때까지.
    while left <= end and arr[left] <= arr[pivot]: # 왼쪽:pivot val 보다 큰거 찾을때 까지 이동
      left+=1
    while right > start and arr[right] >= arr[pivot]: # 오른쪽:pivot val 보다 작은거 찾을 때 까지 이동.
      right-=1
    if left>right: # 더 작은 값과 피봇 교체. ㅇ기서 작은 값은 arr[right]
      arr[right], arr[pivot] = arr[pivot], arr[right]
    else:
      # 따라서 왼쪽에는 pivot보다 작은 것들이 모임. right(<piv_val),left(>piv_val)가 스위치 됨
      arr[left],arr[right] = arr[right],arr[left]
  quick_sort(arr, start, right-1)
  quick_sort(arr, right+1, end)



"""
QuickSort Python
"""

arr = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    if(len(arr)<=1):
        return arr
    pivot=arr[0]
    tail=arr[1:]

    leftSide=[x for x in tail if x<=pivot]
    rightSide=[x for x in  tail if x>pivot]

    return quick_sort(leftSide)+[pivot]+quick_sort(rightSide)

print(arr)



"""
Counting Sort
"""

arr=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(arr)+1)

for i in range(len(arr)):
    count[arr[i]]+=1

for j in range(len(count)):
    for i in range(count[j]):
        print(j, end=' ')


